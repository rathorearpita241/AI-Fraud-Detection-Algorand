import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

data = {
    "tx_amount": np.random.exponential(scale=50, size=n),
    "tx_frequency": np.random.randint(1, 10, size=n),
    "account_age_days": np.random.randint(1, 1000, size=n),
    "is_fraud": np.random.choice([0, 1], size=n, p=[0.95, 0.05])
}

df = pd.DataFrame(data)
df.to_csv("../data/transactions.csv", index=False)

print("Dataset created successfully!")
