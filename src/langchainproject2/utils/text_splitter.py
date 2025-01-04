from langchain_text_splitters import RecursiveCharacterTextSplitter


async def split_text(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=50, is_separator_regex=False
    )
    return text_splitter.split_text(docs)
