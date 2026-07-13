"""
export.py

Export analytics results.
"""

import pandas as pd
import streamlit as st
from io import BytesIO


def export_csv(df, filename="result.csv"):
    """
    Export DataFrame as CSV.
    """

    if not isinstance(df, pd.DataFrame):
        return

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📄 Download CSV",
        data=csv,
        file_name=filename,
        mime="text/csv"
    )


def export_excel(df, filename="result.xlsx"):
    """
    Export DataFrame as Excel.
    """

    if not isinstance(df, pd.DataFrame):
        return

    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Results")

    st.download_button(
        label="📊 Download Excel",
        data=output.getvalue(),
        file_name=filename,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )