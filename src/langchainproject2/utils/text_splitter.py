from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return text_splitter.split_text(docs)
