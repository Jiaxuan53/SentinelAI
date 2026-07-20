import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)
import joblib


# ==========================
# Load Dataset
# ==========================

X = pd.read_csv("data/features.csv")

y_true = pd.read_csv("data/labels.csv")


# Convert label column into array

y_true = y_true["is_attack"]



# ==========================
# Train Isolation Forest
# ==========================

model = IsolationForest(
    contamination=0.4,
    random_state=42
)


model.fit(X)



# ==========================
# Prediction
# ==========================

prediction = model.predict(X)


# Isolation Forest:
# Normal = 1
# Anomaly = -1

prediction_binary = [
    1 if p == -1 else 0
    for p in prediction
]



# ==========================
# Risk Score
# ==========================

scores = model.decision_function(X)


risk_scores = (
    (scores.max()-scores)
    /
    (scores.max()-scores.min())
) * 100


results = X.copy()


results["prediction"] = prediction_binary

results["risk_score"] = risk_scores.round(2)



# ==========================
# Evaluation
# ==========================


print("==========================")
print("Model Evaluation")
print("==========================")


print(
    "Accuracy:",
    round(
        accuracy_score(
            y_true,
            prediction_binary
        ),
        3
    )
)


print(
    "Precision:",
    round(
        precision_score(
            y_true,
            prediction_binary
        ),
        3
    )
)


print(
    "Recall:",
    round(
        recall_score(
            y_true,
            prediction_binary
        ),
        3
    )
)


print(
    "F1 Score:",
    round(
        f1_score(
            y_true,
            prediction_binary
        ),
        3
    )
)



print("\nConfusion Matrix")

print(
    confusion_matrix(
        y_true,
        prediction_binary
    )
)



# ==========================
# Save Model
# ==========================


joblib.dump(
    model,
    "models/isolation_forest.pkl"
)

# Add attack type for analysis

labels = pd.read_csv(
    "data/labels.csv"
)


results["attack_type"] = labels["attack_type"]

results.to_csv(
    "data/prediction_results.csv",
    index=False
)


print("\nModel saved successfully!")