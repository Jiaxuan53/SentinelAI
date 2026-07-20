import pandas as pd


# ==========================
# Generate Risk Explanation
# ==========================

def generate_explanation(row):

    reasons = []


    # API usage anomaly
    if row["api_requests_last_minute"] > 300:
        reasons.append(
            "High API request frequency detected"
        )


    # Financial anomaly
    if row["estimated_cost"] > 50:
        reasons.append(
            "Abnormal API cost consumption detected"
        )


    # Login behaviour
    if row["failed_login_attempts"] > 3:
        reasons.append(
            "Multiple failed login attempts detected"
        )


    # Token sharing behaviour
    if row["unique_ip_count"] > 2:
        reasons.append(
            "Token accessed from multiple IP addresses"
        )


    # Prompt injection
    if row["prompt_injection"] == 1:
        reasons.append(
            "Potential prompt injection detected"
        )


    return reasons



# ==========================
# Risk Level
# ==========================

def get_risk_level(score):

    if score >= 70:
        return "High"

    elif score >= 30:
        return "Medium"

    else:
        return "Low"



# ==========================
# Recommended Action
# ==========================

def recommend_action(row):

    attack_type = row["attack_type"]
    level = row["risk_level"]


    if level == "High":

        if attack_type == "Token Theft":

            return (
                "Revoke compromised token, "
                "terminate active sessions, "
                "review token access logs"
            )


        elif attack_type == "Prompt Injection":

            return (
                "Block malicious prompt, "
                "enable prompt filtering, "
                "review AI interaction history"
            )


        elif attack_type == "Financial Abuse":

            return (
                "Apply API rate limiting, "
                "freeze abnormal usage, "
                "alert finance team"
            )


        elif attack_type == "Account Compromise":

            return (
                "Lock suspicious account, "
                "force MFA verification, "
                "investigate login activity"
            )


        else:

            return (
                "Notify security team "
                "and investigate incident"
            )


    elif level == "Medium":

        return (
            "Require additional verification "
            "and continue monitoring"
        )


    else:

        return "Continue monitoring"


# ==========================
# Main
# ==========================


df = pd.read_csv(
    "data/prediction_results.csv"
)



df["risk_level"] = df["risk_score"].apply(
    get_risk_level
)



df["reasons"] = df.apply(
    generate_explanation,
    axis=1
)



df["recommended_action"] = df.apply(
    recommend_action,
    axis=1
)



df.to_csv(
    "data/final_risk_results.csv",
    index=False
)



print(
    "Explainable AI analysis completed!"
)


print(
    df[[
        "prediction",
        "risk_score",
        "risk_level",
        "recommended_action"
    ]].tail(10)
)