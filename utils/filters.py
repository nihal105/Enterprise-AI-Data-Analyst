"""
filters.py

Interactive dataset filters.
"""

import streamlit as st
import pandas as pd


def apply_filters(df):

    filtered_df = df.copy()

    st.sidebar.header("🎛 Dataset Filters")

    # -----------------------------
    # Date Filter
    # -----------------------------
    if "Date" in filtered_df.columns:

        filtered_df["Date"] = pd.to_datetime(
            filtered_df["Date"],
            errors="coerce"
        )

        min_date = filtered_df["Date"].min()
        max_date = filtered_df["Date"].max()

        if pd.notna(min_date) and pd.notna(max_date):

            date_range = st.sidebar.date_input(
                "📅 Date Range",
                value=(min_date.date(), max_date.date())
            )

            if len(date_range) == 2:

                start_date, end_date = date_range

                filtered_df = filtered_df[
                    (filtered_df["Date"] >= pd.to_datetime(start_date)) &
                    (filtered_df["Date"] <= pd.to_datetime(end_date))
                ]

    # -----------------------------
    # Country Filter
    # -----------------------------
    if "Country" in filtered_df.columns:

        countries = sorted(filtered_df["Country"].dropna().unique())

        selected = st.sidebar.multiselect(
            "🌍 Country",
            countries
        )

        if selected:
            filtered_df = filtered_df[
                filtered_df["Country"].isin(selected)
            ]

    # -----------------------------
    # Product Filter
    # -----------------------------
    if "Product" in filtered_df.columns:

        products = sorted(filtered_df["Product"].dropna().unique())

        selected = st.sidebar.multiselect(
            "📦 Product",
            products
        )

        if selected:
            filtered_df = filtered_df[
                filtered_df["Product"].isin(selected)
            ]

    # -----------------------------
    # Customer Filter
    # -----------------------------
    if "Customer" in filtered_df.columns:

        customers = sorted(filtered_df["Customer"].dropna().unique())

        selected = st.sidebar.multiselect(
            "👤 Customer",
            customers
        )

        if selected:
            filtered_df = filtered_df[
                filtered_df["Customer"].isin(selected)
            ]

    return filtered_df