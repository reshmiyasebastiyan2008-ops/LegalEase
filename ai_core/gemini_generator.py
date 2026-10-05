import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)


class GeminiDocumentGenerator:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-3.8-flash")

    def generate_document(self, document_type, parties, terms, dates):
        prompt = f"""
Create a professional legal document for the given document type.

Document type: {document_type}
Parties involved: {parties}
Terms and conditions: {terms}
Effective dates: {dates}

The document should include all the provided details.
Make sure the document is clear, complete, and professional.
"""

        response = self.model.generate_content(prompt)

        return response.text