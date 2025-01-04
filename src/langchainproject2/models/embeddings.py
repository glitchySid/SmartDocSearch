from langchain_huggingface import HuggingFaceEmbeddings


async def create_embeddings():
    return HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2", encode_kwargs={"normalize_embeddings": True}
    )
