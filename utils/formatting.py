from docx import Document
from fpdf import FPDF


def save_txt(content, filename="legal_document.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

    return filename


def save_docx(content, filename="legal_document.docx"):
    document = Document()

    for paragraph in content.split("\n"):
        document.add_paragraph(paragraph)

    document.save(filename)

    return filename


def save_pdf(content, filename="legal_document.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    # Replace Unicode characters that old FPDF cannot encode
    safe_content = (
        content
        .replace("\u2018", "'")
        .replace("\u2019", "'")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
        .replace("\u2013", "-")
        .replace("\u2014", "-")
        .replace("\u2026", "...")
        .replace("\u00a0", " ")
    )

    for paragraph in safe_content.split("\n"):
        pdf.multi_cell(0, 8, paragraph)
        pdf.ln(2)

    pdf.output(filename)

    return filename