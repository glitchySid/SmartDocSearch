from langchain.schema import Document
from langchain_chroma import Chroma

from ..models.embeddings import create_embeddings


async def create_vector_store(splits):
    text_list = []
    for doc in splits:
        text_list.append(Document(doc))
    vectorstore = await get_vector_store()
    vectorstore.add_documents(text_list)
    return "success"


async def get_vector_store():
    return Chroma(
        collection_name="vector_store",
        persist_directory="./persistent",
        embedding_function=await create_embeddings(),
        collection_metadata={"hnsw:space": "cosine"},
    )
