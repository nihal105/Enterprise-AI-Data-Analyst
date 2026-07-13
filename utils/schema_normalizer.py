"""
schema_normalizer.py

Normalizes uploaded business datasets.
"""

import pandas as pd
from utils.column_mapper import normalize_columns


def normalize_dataset(df):
    """
    Convert uploaded datasets into a common schema.
    """

    mapping = normalize_columns(df)

    # Sales
    if "sales" in mapping:
        df["Sales"] = df[mapping["sales"]]

    elif "quantity" in mapping and "price" in mapping:
        df["Sales"] = (
            df[mapping["quantity"]]
            * df[mapping["price"]]
        )

    # Profit
    if "profit" in mapping:
        df["Profit"] = df[mapping["profit"]]

    # Quantity
    if "quantity" in mapping:
        df["Quantity"] = df[mapping["quantity"]]

    # Customer
    if "customer" in mapping:
        df["Customer"] = df[mapping["customer"]]

    # Product
    if "product" in mapping:
        df["Product"] = df[mapping["product"]]

    # Date
    if "date" in mapping:
        df["Date"] = pd.to_datetime(
            df[mapping["date"]],
            errors="coerce"
        )

    return df