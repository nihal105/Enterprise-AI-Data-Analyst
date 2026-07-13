"""
data_loader.py

Global DataFrame Manager
"""

import pandas as pd

# Store the currently loaded dataset
current_df = None


def set_dataframe(df):
    """
    Save the currently loaded DataFrame.
    """
    global current_df
    current_df = df


def get_dataframe():
    """
    Return the currently loaded DataFrame.
    """
    return current_df


def load_data():
    """
    Return the uploaded dataset.
    If none is uploaded, load the default dataset.
    """
    global current_df

    if current_df is not None:
        return current_df

    return pd.read_csv("datasets/business/Global Superstore.csv")