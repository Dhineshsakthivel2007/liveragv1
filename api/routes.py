from fastapi import APIRouter
from rag.qurey import RAGRetriever
from rag.embeddings import embedding_manager
from rag.llm import generate_answer
from rag.vectorstore import vectorstore
router=APIRouter()
rag_retriver=RAGRetriever(vectorstore,embedding_manager)
@router.post("/ask")
def ask(question:str):
    docs=rag_retriver.retrieve(query=question,top_k=5)
    if not docs:
        return {
            "question":question,
            "answer":"no relavant information found",
            "sources":[]
        }
    context="\n\n".join(f"-{doc['content']}" for doc in docs)
    prompt=f"""You are a news summarization assistant.

        TASK:
        Summarize the latest technology news into a short, clear answer.
        DO NOT ask questions.
        DO NOT list Q&A.
        DO NOT invent information.
        ONLY use the provided news articles.

        FORMAT:
        - Start with 1–2 sentence summary
        - Then list 3–5 bullet-point headlines
        News Articles:{context} USER QUERY:{question} answer:"""
    answer=generate_answer(prompt)
    return{
        "question":question,
        "answer":answer,
        "sources":[{
            "rank":doc["rank"],
            "distance":doc["distance"]
        } for doc in docs]
    }