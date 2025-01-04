from langchain import hub


def load_prompt():
    return hub.pull("rlm/rag-prompt")
