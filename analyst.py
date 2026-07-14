"""
analyst.py

Enterprise AI Data Analyst
"""

import streamlit as st
import pandas as pd

from transformer.predict import predict_intent

from analytics.router import execute_intent
from analytics.smart_router import execute_parsed_query
from analytics.dynamic_router import execute_dynamic_query

from utils.data_loader import set_dataframe
from utils.dataset_detector import analyze_dataset
from utils.column_mapper import normalize_columns
from utils.schema_normalizer import normalize_dataset
from utils.filters import apply_filters
from utils.export import export_csv, export_excel
from analytics.kpi_dashboard import show_kpis

from visualization.auto_visualizer import visualize
from analytics.smart_insights import generate_smart_insights
from nlp.query_parser import parse_query
from utils.pdf_export import export_pdf

from utils.chat_history import (
    initialize_chat,
    add_user_message,
    add_ai_message,
    clear_chat,
)

# =================================================
# Page Configuration
# =================================================

st.set_page_config(
    page_title="Enterprise AI Data Analyst",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
)

# =================================================
# Global Styling (minimal)
# =================================================

st.markdown("""
<style>
    /* ---------- Base ---------- */
    html, body, [class*="css"] {
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1100px;
    }

    /* ---------- Section headers ---------- */
    .section-title {
        font-size: 1.15rem;
        font-weight: 600;
        color: var(--text-color);
        margin: 0.4rem 0 0.7rem 0;
        padding-left: 0.6rem;
        border-left: 3px solid #3B82F6;
    }

    /* ---------- Metrics: plain, no boxes ---------- */
    div[data-testid="stMetric"] {
        background: transparent;
        border: none;
        border-bottom: 1px solid rgba(128, 128, 128, 0.2);
        border-radius: 0;
        padding: 0.4rem 0.2rem;
        text-align: left;
    }
    div[data-testid="stMetricLabel"] {
        font-weight: 400;
        color: var(--text-color);
        opacity: 0.6;
        font-size: 0.85rem;
    }
    div[data-testid="stMetricValue"] {
        color: var(--text-color);
        font-weight: 500;
        font-size: 1.4rem;
    }

    /* ---------- Buttons ---------- */
    .stButton > button, .stDownloadButton > button {
        border-radius: 6px;
        font-weight: 400;
        border: 1px solid rgba(128, 128, 128, 0.3);
    }
    .stButton > button:hover, .stDownloadButton > button:hover {
        border-color: #3B82F6;
        color: #3B82F6;
    }
    .stButton > button:focus, .stDownloadButton > button:focus,
    .stButton > button:focus:not(:active), .stDownloadButton > button:focus:not(:active) {
        box-shadow: 0 0 0 1px #3B82F6;
        border-color: #3B82F6;
        color: inherit;
    }

    /* ---------- File uploader ---------- */
    [data-testid="stFileUploaderDropzone"] {
        border-radius: 10px;
        border: 1px dashed rgba(128, 128, 128, 0.35) !important;
    }
    [data-testid="stFileUploaderDropzone"] button {
        border-radius: 6px;
    }
    [data-testid="stFileUploaderDropzone"] button:focus,
    [data-testid="stFileUploaderDropzone"] button:focus:not(:active) {
        box-shadow: 0 0 0 1px #3B82F6;
        border-color: #3B82F6;
    }

    /* ---------- Chat input ---------- */
    [data-testid="stChatInput"] {
        border-radius: 10px;
    }
    [data-testid="stChatInput"]:focus-within {
        box-shadow: 0 0 0 1px #3B82F6;
        border-radius: 10px;
    }

    /* ---------- Expander ---------- */
    [data-testid="stExpander"] {
        border-radius: 8px;
        border: 1px solid rgba(128, 128, 128, 0.25) !important;
    }

    /* ---------- Sidebar ---------- */
    section[data-testid="stSidebar"] h2 {
        border-left: 3px solid #3B82F6;
        padding-left: 0.6rem;
    }

    /* ---------- Divider spacing ---------- */
    hr {
        margin: 1.4rem 0;
        opacity: 0.15;
    }

    /* ---------- Footer ---------- */
    .footer {
        text-align: center;
        color: var(--text-color);
        opacity: 0.4;
        font-size: 0.78rem;
        padding-top: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# =================================================
# Sidebar
# =================================================

with st.sidebar:
    st.markdown("## AI Analyst")
    st.caption("Enterprise Business Intelligence")

    st.success("System Ready")

    st.markdown("---")

    st.markdown("**Version**  \n1.0")
    st.markdown("**Developers**  \nNihaall · Shifana · Murshid")
    st.markdown("**Project**  \nFinal Year Deep Learning Project")

    st.markdown("---")
    st.caption("Powered by Transformer NLP + Streamlit")

# =================================================
# Hero Header
# =================================================

st.title("Enterprise AI Data Analyst")
st.caption("Analyze business datasets using AI, NLP, and interactive analytics.")

# =================================================
# Chat History
# =================================================

initialize_chat()

hist_col1, hist_col2 = st.columns([9, 1])
with hist_col1:
    st.markdown('<div class="section-title">Conversation</div>', unsafe_allow_html=True)
with hist_col2:
    if st.button("Clear", use_container_width=True):
        clear_chat()
        st.rerun()

if st.session_state.messages:
    with st.container():
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
else:
    st.caption("No conversation yet — upload a dataset and ask a question below to get started.")

st.divider()

# =================================================
# Upload Dataset
# =================================================

st.markdown('<div class="section-title">Dataset Management</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload a CSV or Excel dataset",
    type=["csv", "xlsx", "xls"],
    label_visibility="visible",
)

df = None

if uploaded_file is not None:

    try:

        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)

        elif uploaded_file.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file, engine="openpyxl")

        else:
            df = pd.read_excel(uploaded_file)

        # Normalize
        df = normalize_dataset(df)

        # Apply Filters
        df = apply_filters(df)

        # Save DataFrame
        set_dataframe(df)

        # Dataset Information
        info = analyze_dataset(df)
        mapping = normalize_columns(df)

        st.success(f"**{uploaded_file.name}** loaded successfully.")

        # -----------------------------------
        # KPI Dashboard
        # -----------------------------------
        show_kpis()

        st.divider()

        st.markdown('<div class="section-title">Dataset Summary</div>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Rows", f"{info['rows']:,}")

        with col2:
            st.metric("Columns", info["columns"])

        with col3:
            st.metric("File", uploaded_file.name)

        with st.expander("View Detected Columns"):
            st.json(mapping)

        with st.expander("Dataset Preview", expanded=False):
            st.caption(f"Showing first **{min(20, len(df))}** of **{len(df):,}** rows")
            st.dataframe(
                df.head(20),
                use_container_width=True,
                height=350,
            )

    except Exception as e:
        st.error(f"Error loading file: {str(e)}")

st.divider()

# =================================================
# Chat Input
# =================================================

st.markdown('<div class="section-title">AI Business Assistant</div>', unsafe_allow_html=True)

question = st.chat_input("Ask a business question about your data...")

# =================================================
# Ask AI
# =================================================

if question:

    if df is None:
        st.warning("Please upload a dataset first.")

    else:

        add_user_message(question)

        with st.chat_message("user"):
            st.write(question)

        try:

            # -----------------------------
            # Intent Prediction
            # -----------------------------
            intent, confidence = predict_intent(question)

            # -----------------------------
            # Query Parsing
            # -----------------------------
            parsed_query = parse_query(question)

            # -----------------------------
            # Dynamic Router
            # -----------------------------
            result = execute_dynamic_query(parsed_query)

            # -----------------------------
            # Smart Router
            # -----------------------------
            if result is None:
                result = execute_parsed_query(parsed_query)

            # -----------------------------
            # Transformer Router
            # -----------------------------
            if result is None:
                result = execute_intent(intent)

            # -----------------------------
            # Dashboard
            # -----------------------------
            if intent == "dashboard_summary":
                add_ai_message(question)
                st.stop()

            # -----------------------------
            # Assistant Response
            # -----------------------------
            with st.chat_message("assistant"):

                st.markdown('<div class="section-title">AI Prediction</div>', unsafe_allow_html=True)

                pcol1, pcol2 = st.columns(2)
                with pcol1:
                    st.success(f"Intent: **{intent}**")
                with pcol2:
                    st.info(f"Confidence: **{confidence:.2f}%**")

                with st.expander("Query Analysis"):
                    st.json(parsed_query)

                st.divider()

                st.markdown('<div class="section-title">Business Analysis</div>', unsafe_allow_html=True)

                if result is not None:

                    # Visualization
                    visualize(intent, result)

                    # Smart AI Insights
                    insights = generate_smart_insights(intent, result)

                    if insights:
                        st.divider()
                        st.markdown('<div class="section-title">AI Business Insights</div>', unsafe_allow_html=True)

                        for insight in insights:
                            st.info(insight)

                    # Export Results
                    if isinstance(result, pd.DataFrame):

                        st.divider()
                        st.markdown('<div class="section-title">Export Reports</div>', unsafe_allow_html=True)

                        col1, col2, col3 = st.columns(3)

                        with col1:
                            export_csv(result)

                        with col2:
                            export_excel(result)

                        with col3:
                            export_pdf(
                                question=question,
                                intent=intent,
                                result=result,
                                insights=insights
                            )

                    add_ai_message(question)

                else:
                    st.warning("No result found for this query.")

        except Exception as e:
            st.error(f"{e}")
            st.divider()

# =================================================
# Footer
# =================================================

st.divider()

with st.expander("About This Project"):

    st.markdown("""
### Enterprise AI Data Analyst

A Deep Learning based Business Analytics System powered by Transformer NLP.

**Features**

| | |
|---|---|
| Transformer Intent Detection | Interactive Dashboard |
| Automatic Visualizations | AI Business Insights |
| PDF Reports | CSV & Excel Export |

---

**Version:** 1.0  
**Developed By:** 
- Nihaall 
- Shifana 
- Murshid  
**Project:** Final Year Deep Learning Project
""")

st.markdown(
    '<div class="footer">Enterprise AI Data Analyst &nbsp;·&nbsp; Final Year Deep Learning Project &nbsp;·&nbsp; Version 1.0 &nbsp;·&nbsp; © 2026</div>',
    unsafe_allow_html=True,
)