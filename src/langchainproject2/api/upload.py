from fastapi import APIRouter, UploadFile,Form,HTTPException
from typing import List
from ..utils.pdf_loader import load_text
from ..utils.text_splitter import split_text
from ..utils.vector_store import create_vector_store

router = APIRouter()


@router.post("/upload/")
async def upload( files: List[UploadFile], collection_name: str = Form(...), ):
    try:
        all_texts = []
        
        # Process each file
        for file in files:
            # Ensure the uploaded file is a PDF
            if not file.filename.endswith(".pdf"):
                raise HTTPException(status_code=400, detail=f"File {file.filename} is not a PDF")
            
            # Extract text from the PDF
            text = await load_text(file)
            all_texts.append({"filename": file.filename, "text": text})
        
        # Combine all texts or process them individually (based on your logic)
        combined_texts = [item["text"] for item in all_texts]
        splits = [await split_text(text) for text in combined_texts]
        
        # Create vector store for all splits
        for split in splits:
            _ = await create_vector_store(collection_name, split)
        
        return {"message": "Files uploaded successfully", "files_processed": len(files)}
    
    except Exception as e:
        return {"error": str(e)}