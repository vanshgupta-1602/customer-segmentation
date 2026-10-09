import streamlit as st
from pypdf import PdfReader
import re

st.set_page_config(
    page_title="Financial Report Analyzer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Financial Report Analyzer")
st.caption("PDF-based financial metrics and year-over-year analysis")

uploaded_file = st.file_uploader(
    "Upload a financial report (PDF)",
    type=["pdf"]
)

def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    return "\n".join(page.extract_text() or "" for page in reader.pages)

def find_amount(text, pattern):
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return float(match.group(1).replace(",", ""))
    return None

def format_amount(value):
    return f"₹{value:,.0f} crore" if value is not None else "Not found"

if uploaded_file:
    try:
        text = extract_text(uploaded_file)
        st.text(repr(text[:3000]))

        if not text.strip():
            st.error("No readable text found in this PDF.")
            st.stop()

        st.success("PDF uploaded successfully!")

        # Extract financial figures from the sample report format
        revenue_24 = find_amount(
            text, r"Revenue\s+([0-9,]+)\s+crore"
        )
        revenue_25 = find_amount(
            text, r"Revenue\s+[0-9,]+\s+crore\s+([0-9,]+)\s+crore"
        )

        profit_24 = find_amount(
            text, r"Net Profit\s+([0-9,]+)\s+crore"
        )
        profit_25 = find_amount(
            text, r"Net Profit\s+[0-9,]+\s+crore\s+([0-9,]+)\s+crore"
        )

        debt_24 = find_amount(
            text, r"Total Debt\s+([0-9,]+)\s+crore"
        )
        debt_25 = find_amount(
            text, r"Total Debt\s+[0-9,]+\s+crore\s+([0-9,]+)\s+crore"
        )

        cash_24 = find_amount(
            text, r"Cash\s*&\s*Equivalents\s+([0-9,]+)\s+crore"
        )
        cash_25 = find_amount(
            text, r"Cash\s*&\s*Equivalents\s+[0-9,]+\s+crore\s+([0-9,]+)\s+crore"
        )

        def growth(old, new):
            if old is not None and new is not None and old != 0:
                return (new - old) / old * 100
            return None

        st.subheader("Financial Overview")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**FY 2024–25**")
            st.metric("Revenue", format_amount(revenue_24))
            st.metric("Net Profit", format_amount(profit_24))
            st.metric("Total Debt", format_amount(debt_24))
            st.metric("Cash", format_amount(cash_24))

        with col2:
            st.markdown("**FY 2025–26**")
            st.metric(
                "Revenue", format_amount(revenue_25),
                f"{growth(revenue_24, revenue_25):.1f}%"
                if growth(revenue_24, revenue_25) is not None else None
            )
            st.metric(
                "Net Profit", format_amount(profit_25),
                f"{growth(profit_24, profit_25):.1f}%"
                if growth(profit_24, profit_25) is not None else None
            )
            st.metric(
                "Total Debt", format_amount(debt_25),
                f"{debt_25 - debt_24:,.0f} crore"
                if debt_24 is not None and debt_25 is not None else None,
                delta_color="inverse"
            )
            st.metric(
                "Cash", format_amount(cash_25),
                f"{cash_25 - cash_24:,.0f} crore"
                if cash_24 is not None and cash_25 is not None else None
            )

        st.subheader("Automated Insights")

        rev_growth = growth(revenue_24, revenue_25)
        profit_growth = growth(profit_24, profit_25)

        if rev_growth is not None:
            st.write(f"- Revenue changed by **{rev_growth:.2f}%** year over year.")

        if profit_growth is not None:
            st.write(f"- Net profit changed by **{profit_growth:.2f}%** year over year.")

        if debt_24 is not None and debt_25 is not None:
            change = debt_25 - debt_24
            st.write(
                f"- Total debt {'increased' if change > 0 else 'decreased' if change < 0 else 'did not change'} "
                f"by **₹{abs(change):,.0f} crore**."
            )

        if cash_24 is not None and cash_25 is not None:
            change = cash_25 - cash_24
            st.write(
                f"- Cash {'increased' if change > 0 else 'decreased' if change < 0 else 'did not change'} "
                f"by **₹{abs(change):,.0f} crore**."
            )

        with st.expander("View extracted PDF text"):
            st.text(text[:15000])

        st.caption(
            "Note: Automated extraction uses expected financial-table formats. "
            "Always verify extracted figures against the original report."
        )

    except Exception as error:
        st.error(f"Could not analyze this PDF: {error}")

              