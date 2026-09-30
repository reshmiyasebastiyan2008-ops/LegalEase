import streamlit as st
import requests
from utils.formatting import save_txt, save_docx, save_pdf


st.title("LegalEase - AI Legal Document Generator")

document_type = st.selectbox(
    "Document Type",
    [
        "Employment Contract",
        "NDA",
        "Lease Agreement"
    ]
)

parties = st.text_input("Parties Involved")

terms = st.text_area("Terms and Conditions")

effective_date = st.date_input("Effective Date")


if st.button("Generate Document"):

    parties = parties.strip()
    terms = terms.strip()
    dates = str(effective_date)

    if not parties or not terms:
        st.warning("Please enter all required details.")
        st.stop()

    try:
        response = requests.post(
            "http://127.0.0.1:8000/generate",
            json={
                "document_type": document_type,
                "parties": parties,
                "terms": terms,
                "dates": dates
            },
            timeout=120
        )

        if response.status_code != 200:
            st.error("API Error: " + response.text)
            st.stop()

        document = response.json()["document"]

        st.subheader("Generated Document")

        st.text_area(
            "Document Preview",
            document,
            height=500
        )

        save_txt(document)
        save_docx(document)
        save_pdf(document)

        st.success("Document generated successfully!")

        col1, col2, col3 = st.columns(3)

        with col1:
            with open("legal_document.txt", "rb") as file:
                st.download_button(
                    "Download TXT",
                    file,
                    file_name="legal_document.txt",
                    mime="text/plain"
                )

        with col2:
            with open("legal_document.docx", "rb") as file:
                st.download_button(
                    "Download DOCX",
                    file,
                    file_name="legal_document.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )

        with col3:
            with open("legal_document.pdf", "rb") as file:
                st.download_button(
                    "Download PDF",
                    file,
                    file_name="legal_document.pdf",
                    mime="application/pdf"
                )

    except requests.exceptions.RequestException:
        st.error(
            "Could not connect to the backend. "
            "Make sure FastAPI is running on http://127.0.0.1:8000"
        )