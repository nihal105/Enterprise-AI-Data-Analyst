import pandas as pd

# Load dataset
df = pd.read_csv(
    "datasets/business/Global Superstore.csv",
    encoding="latin1"
)

print("=" * 60)
print("COLUMN DETAILS")
print("=" * 60)

for col in df.columns:
    print(f"\n📌 {col}")
    print("-" * 40)
    print(df[col].head())