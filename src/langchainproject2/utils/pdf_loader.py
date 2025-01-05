from langchain_community.document_loaders import PyPDFLoader
from io import BytesIO
from pdfplumber import PDF
from fastapi import UploadFile, HTTPException

async def load_pdf(file_path):
    return PyPDFLoader(file_path)


# Function to extract text from a single PDF
async def load_text(file: UploadFile) -> str:
    # Read file content into memory buffer
    file_content = await file.read()
    try:
        with PDF(BytesIO(file_content)) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() or ""
            return text
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing file {file.filename}: {str(e)}")
