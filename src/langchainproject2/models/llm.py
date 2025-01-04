from langchain_google_genai import ChatGoogleGenerativeAI


def create_llm():
    return ChatGoogleGenerativeAI(model="gemini-1.5-flash")
