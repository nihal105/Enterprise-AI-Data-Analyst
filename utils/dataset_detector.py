"""
dataset_detector.py

Detects dataset information.
"""

import pandas as pd


def analyze_dataset(df):
    """
    Analyze uploaded dataset.

    Returns a dictionary containing useful metadata.
    """

    info = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns),
        "numeric_columns": list(df.select_dtypes(include="number").columns),
        "date_columns": list(df.select_dtypes(include="datetime").columns),
        "text_columns": list(df.select_dtypes(include="object").columns),
    }

    return info