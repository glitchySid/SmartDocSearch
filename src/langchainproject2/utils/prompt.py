from langchain import hub


async def load_prompt():
    return hub.pull("rlm/rag-prompt")
