from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


async def create_rag_chain(retriever, prompt, llm):
    print("creating chain")
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain
