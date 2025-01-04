from langchain_google_genai import ChatGoogleGenerativeAI


async def create_llm():
    return ChatGoogleGenerativeAI(model="gemini-1.5-flash")
