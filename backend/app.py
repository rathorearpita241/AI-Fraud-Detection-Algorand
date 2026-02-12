from fastapi import FastAPI
import joblib
import numpy as np
from algorand_tx import send_algorand_transaction

app = FastAPI(title="AI Fraud Detection + Algorand API")

# Load trained ML model
model = joblib.load("fraud_model.pkl")


@app.get("/")
def home():
    return {"message": "Fraud Detection + Algorand API Running"}


@app.post("/check_transaction")
def check_transaction(
    tx_amount: float,
    tx_frequency: int,
    account_age_days: int,
    receiver_address: str
):
    """
    Hybrid Fraud Detection:
    1. Hard safety rule
    2. ML probability check
    3. If safe → send to Algorand blockchain
    """

    # 🚨 HARD SAFETY RULE (absolute block)
    if tx_amount > 4000:
        return {
            "status": "BLOCKED",
            "fraud_probability": 1.0,
            "reason": "Transaction amount exceeds safe limit"
        }

    # ML Evaluation
    features = np.array([[tx_amount, tx_frequency, account_age_days]])
    fraud_prob = model.predict_proba(features)[0][1]

    # AI-based fraud decision
    if fraud_prob > 0.30:
        return {
            "status": "BLOCKED",
            "fraud_probability": round(float(fraud_prob), 3),
            "reason": "AI detected fraudulent behavior"
        }

    # ✅ SAFE → Execute Algorand transaction
    try:
        txid = send_algorand_transaction(
            receiver=receiver_address,
            amount_microalgos=int(tx_amount * 1_000_000)
        )

        return {
            "status": "APPROVED",
            "fraud_probability": round(float(fraud_prob), 3),
            "algorand_tx_id": txid,
            "reason": "Transaction successfully executed on Algorand"
        }

    except Exception as e:
        return {
            "status": "ERROR",
            "message": str(e)
        }
