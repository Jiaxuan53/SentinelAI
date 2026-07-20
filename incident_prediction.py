import pandas as pd


# ==========================
# Incident Prediction Engine
# ==========================


def predict_incident(row):

    risk_score = row["risk_score"]
    attack_type = row["attack_type"]
    probability = calculate_probability(risk_score)

    # High risk incidents

    if risk_score >= 80:

        if attack_type == "Token Theft":

            return (
                f"{probability}%",
                "Possible Token Theft Incident",
                "Likely unauthorized API access within short period"
            )


        elif attack_type == "Prompt Injection":

            return (
                f"{probability}%",
                "Possible AI Security Incident",
                "Potential malicious prompt manipulation detected"
            )


        elif attack_type == "Financial Abuse":

            return (
                f"{probability}%",
                "Possible Financial Risk Incident",
                "Potential abnormal AI service cost escalation"
            )


        elif attack_type == "Account Compromise":

            return (
                f"{probability}%",
                "Possible Account Security Incident",
                "Potential compromised user account activity"
            )


    elif risk_score >= 50:

        return (
            "Medium",
            "Potential Security Incident",
            "Suspicious behaviour requires monitoring"
        )


    else:

        return (
            "Low",
            "No Immediate Incident",
            "Activity appears normal"
        )

def calculate_probability(score):

    probability = score

    if probability > 99:
        probability = 99

    if probability < 5:
        probability = 5

    return round(probability,1)

# ==========================
# Load Results
# ==========================


df = pd.read_csv(
    "data/final_risk_results.csv"
)



# Apply prediction

prediction_results = df.apply(
    predict_incident,
    axis=1
)



df[
    [
        "incident_probability",
        "predicted_incident",
        "incident_reason"
    ]
] = pd.DataFrame(
    prediction_results.tolist(),
    index=df.index
)



# Save


df.to_csv(
    "data/incident_prediction_results.csv",
    index=False
)



print(
    "Incident prediction completed!"
)


print(
    df[
        [
            "attack_type",
            "risk_score",
            "incident_probability",
            "predicted_incident"
        ]
    ].tail(10)
)