import json
import pandas as pd


# ==========================
# Load Logs
# ==========================

with open(
    "logs/auth_logs.json",
    "r"
) as f:

    logs = json.load(f)


df = pd.DataFrame(logs)



# ==========================
# Save Labels
# ==========================

labels = df[
    [
        "is_attack",
        "attack_type"
    ]
]


labels.to_csv(
    "data/labels.csv",
    index=False
)



# ==========================
# Select AI Features
# ==========================

features = df[
    [
        "api_requests_last_minute",
        "estimated_cost",
        "failed_login_attempts",
        "session_duration",
        "prompt_length",
        "unique_ip_count",
        "contains_prompt_injection"
    ]
].copy()



# Rename

features.rename(
    columns={
        "contains_prompt_injection":
        "prompt_injection"
    },
    inplace=True
)



# ==========================
# Save Features
# ==========================

features.to_csv(
    "data/features.csv",
    index=False
)


print(
    "Feature engineering completed!"
)

print(
    "Features:",
    features.shape
)

print(
    "Labels:",
    labels.shape
)