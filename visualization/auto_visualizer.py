"""
auto_visualizer.py

Automatically selects the best visualization
based on the predicted intent and result.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def visualize(intent, result):
    """
    Automatically visualize analytics results.
    """

    # -----------------------------
    # Plotly Figure
    # -----------------------------
    if isinstance(result, go.Figure):
        st.plotly_chart(result, use_container_width=True)
        return

    # -----------------------------
    # DataFrame
    # -----------------------------
    if isinstance(result, pd.DataFrame):

        st.dataframe(result, use_container_width=True)

        if len(result.columns) < 2:
            return

        # Monthly / Yearly Sales / Profit Growth
        if intent in [
            "monthly_sales",
            "yearly_sales",
            "profit_growth"
        ]:

            fig = px.line(
                result,
                x=result.columns[0],
                y=result.columns[1],
                markers=True,
                title=intent.replace("_", " ").title()
            )

            st.plotly_chart(fig, use_container_width=True)
            return

        # Top Products / Customers
        elif intent in ["top_products", "top_customers"]:

            fig = px.bar(
                result,
                x=result.columns[0],
                y=result.columns[1],
                color=result.columns[1],
                title=intent.replace("_", " ").title()
            )

            st.plotly_chart(fig, use_container_width=True)
            return

        # Generic Bar Chart
        elif len(result.columns) == 2:

            fig = px.bar(
                result,
                x=result.columns[0],
                y=result.columns[1],
                title="Analysis"
            )

            st.plotly_chart(fig, use_container_width=True)
            return

        return

    # -----------------------------
    # String Result
    # -----------------------------
    if isinstance(result, str):
        st.success(result)
        return

    # -----------------------------
    # Anything Else
    # -----------------------------
    st.write(result)