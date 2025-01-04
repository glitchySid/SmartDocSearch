from langchain_community.document_loaders import PyPDFLoader
from pdfplumber import open


def load_pdf(file_path):
    return PyPDFLoader(file_path)


def load_text(file_path):
    file = open(file_path)
    pages = file.pages
    text = ""
    for page in pages:
        text += page.extract_text()
    return text
