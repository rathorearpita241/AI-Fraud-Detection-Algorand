from algosdk import transaction, account
from algosdk.v2client import algod
from algorand_config import algod_client

# Temporary sender account (for hackathon demo)
#  NEVER hardcode keys in production
SENDER_PRIVATE_KEY, SENDER_ADDRESS = account.generate_account()


def send_algorand_transaction(receiver: str, amount_microalgos: int):
    """
    Sends Algorand transaction after fraud check
    """
    params = algod_client.suggested_params()

    txn = transaction.PaymentTxn(
        sender=SENDER_ADDRESS,
        sp=params,
        receiver=receiver,
        amt=amount_microalgos
    )

    signed_txn = txn.sign(SENDER_PRIVATE_KEY)
    txid = algod_client.send_transaction(signed_txn)

    return txid

