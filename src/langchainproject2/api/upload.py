from fastapi import APIRouter, UploadFile

from ..utils.pdf_loader import load_text
from ..utils.text_splitter import split_text
from ..utils.vector_store import create_vector_store

router = APIRouter()


@router.post("/uploadfile/")
async def upload_file(file: UploadFile):
    try:
        text = load_text(file.file)
        splits = split_text(text)
        _ = create_vector_store(splits)
        return {"message": "File uploaded successfully"}
    except Exception as e:
        print(e)
        return {"error": str(e)}
