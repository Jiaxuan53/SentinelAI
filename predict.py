import json
import joblib
import pandas as pd

# Load trained AI model
model = joblib.load("models/isolation_forest.pkl")

# Read latest enterprise logs
with open("logs/auth_logs.json", "r") as f:
    logs = json.load(f)

df = pd.DataFrame(logs)

# Select the same features used during training
features = df[[
    "api_requests_last_minute",
    "estimated_cost",
    "failed_login_attempts",
    "session_duration",
    "prompt_length",
    "unique_ip_count",
    "contains_prompt_injection"
]].copy()

features.rename(columns={
    "contains_prompt_injection": "prompt_injection"
}, inplace=True)

# Predict
prediction = model.predict(features)

# Risk Score
score = model.decision_function(features)

risk_score = ((score.max()-score)/(score.max()-score.min()))*100

df["prediction"] = prediction

df["prediction"] = df["prediction"].replace({
    1:"Normal",
    -1:"Attack"
})

df["risk_score"] = risk_score.round(1)

print(df[[
    "user_id",
    "country",
    "api_requests_last_minute",
    "prediction",
    "risk_score"
]].head(20))

def recommend_action(score):

    if score >= 80:
        return "Immediately revoke token and notify Security Team"

    elif score >= 50:
        return "Require MFA verification"

    else:
        return "Continue Monitoring"


df["recommended_action"] = df["risk_score"].apply(recommend_action)

print(df[[
    "user_id",
    "prediction",
    "risk_score",
    "recommended_action"
]].head(20))