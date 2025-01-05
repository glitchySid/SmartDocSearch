from fastapi import APIRouter,Body

from ..chains.rag_chain import create_rag_chain
from ..models.llm import create_llm
from ..utils.prompt import load_prompt
from ..utils.retriever import create_retriever
from ..utils.vector_store import get_vector_store

router = APIRouter()


@router.post("/ask/{session_id}")
async def give_output(session_id:str,question: str=Body(...)):
    try:
        vectorstore = await get_vector_store(collection_name=session_id)
        llm = await create_llm()
        retriever = await create_retriever(vectorstore)
        prompt = await load_prompt()
        rag_chain = await create_rag_chain(retriever, prompt, llm)
        rag_output = rag_chain.invoke(question)
        print(rag_output)
        return {"output": rag_output}
    except Exception as e:
        return {"error": str(e)}