"""
reconstruct_dates.py

Reconstructs Order Date and Ship Date
using the existing Year column.
"""

import random
import pandas as pd

random.seed(42)  # Makes the reconstruction reproducible

# Load dataset
df = pd.read_csv("datasets/business/Global Superstore.csv")


def random_date(year):
    month = random.randint(1, 12)
    day = random.randint(1, 28)   # Safe for every month
    return pd.Timestamp(year=year, month=month, day=day)


# Generate Order Dates
df["Order Date"] = df["Year"].apply(random_date)

# Generate Ship Dates (1–7 days after Order Date)
df["Ship Date"] = (
    df["Order Date"]
    + pd.to_timedelta(
        [random.randint(1, 7) for _ in range(len(df))],
        unit="D"
    )
)

# Save the updated dataset
df.to_csv(
    "datasets/business/Global Superstore.csv",
    index=False
)

print("✅ Dates reconstructed successfully.")
print(df[["Order Date", "Ship Date", "Year"]].head())