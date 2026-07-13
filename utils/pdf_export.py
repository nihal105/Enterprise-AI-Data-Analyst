"""
pdf_export.py

Professional PDF Report Generator using ReportLab
"""

import streamlit as st
import pandas as pd
from io import BytesIO
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


def export_pdf(question, intent, result, insights):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    # ------------------------------------------------
    # Title
    # ------------------------------------------------

    story.append(
        Paragraph("<b>Enterprise AI Data Analyst</b>", styles["Title"])
    )

    story.append(
        Paragraph(
            f"Generated: {datetime.now().strftime('%d-%m-%Y %H:%M')}",
            styles["Normal"],
        )
    )

    story.append(Spacer(1, 15))

    # ------------------------------------------------
    # Business Question
    # ------------------------------------------------

    story.append(
        Paragraph("<b>Business Question</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(question, styles["BodyText"])
    )

    story.append(Spacer(1, 10))

    # ------------------------------------------------
    # Intent
    # ------------------------------------------------

    story.append(
        Paragraph("<b>Predicted Intent</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(intent, styles["BodyText"])
    )

    story.append(Spacer(1, 10))

    # ------------------------------------------------
    # Result Summary
    # ------------------------------------------------

    story.append(
        Paragraph("<b>Result Summary</b>", styles["Heading2"])
    )

    if isinstance(result, pd.DataFrame):

        story.append(
            Paragraph(f"Rows Returned: {len(result)}", styles["BodyText"])
        )

        story.append(
            Paragraph(f"Columns: {len(result.columns)}", styles["BodyText"])
        )

        story.append(Spacer(1, 8))

        # First 10 rows only
        preview = result.head(10).copy()

        # Convert to string
        preview = preview.astype(str)

        # Truncate long text (Pandas 3 compatible)
        for col in preview.columns:
            preview[col] = preview[col].apply(
                lambda x: x[:25] + "..." if len(x) > 25 else x
            )

        # Build table
        table_data = [list(preview.columns)]

        for _, row in preview.iterrows():
            table_data.append(row.tolist())

        table = Table(table_data, repeatRows=1)

        table.setStyle(
            TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
                ("TOPPADDING", (0, 1), (-1, -1), 4),
            ])
        )

        story.append(table)

    else:

        story.append(
            Paragraph(str(result), styles["BodyText"])
        )

    story.append(Spacer(1, 15))

    # ------------------------------------------------
    # AI Insights
    # ------------------------------------------------

    story.append(
        Paragraph("<b>AI Business Insights</b>", styles["Heading2"])
    )

    if insights:

        for insight in insights:
            story.append(
                Paragraph(f"• {insight}", styles["BodyText"])
            )

    else:

        story.append(
            Paragraph("No insights available.", styles["BodyText"])
        )

    # ------------------------------------------------
    # Build PDF
    # ------------------------------------------------

    doc.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    st.download_button(
        label="📄 Download PDF Report",
        data=pdf,
        file_name="Business_Report.pdf",
        mime="application/pdf",
    )