import csv
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

X = []
y = []

# Load dataset
with open("../data/transactions.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        X.append([
            float(row["tx_amount"]),
            int(row["tx_frequency"]),
            int(row["account_age_days"])
        ])
        y.append(int(row["is_fraud"]))

X = np.array(X)
y = np.array(y)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
acc = accuracy_score(y_test, preds)

print(f"Model Accuracy: {acc * 100:.2f}%")

# Save model
joblib.dump(model, "../backend/fraud_model.pkl")
print("Model saved to backend/fraud_model.pkl")
