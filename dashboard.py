
import streamlit as st
from pypdf import PdfReader

st.title("AI Financial Report Analyzer")
st.write("Upload a PDF to analyze its financial report.")

uploaded_file = st.file_uploader("Choose a PDF", type=["pdf"])

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    text = "\n".join(page.extract_text() or "" for page in reader.pages)

    st.success("PDF uploaded successfully!")
    st.subheader("Extracted Financial Report")

    if text.strip():
        st.text_area("Report contents", text, height=400)

        st.download_button(
            "Download extracted text",
            data=text,
            file_name="financial_report.txt"
        )
    else:
        st.warning("No readable text found in this PDF.")
        

