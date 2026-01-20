from fastapi import APIRouter
from pydantic import BaseModel

from rag.qurey import RAGRetriever
from rag.embeddings import embedding_manager
from rag.llm import generate_answer
from rag.vectorstore import vectorstore

router = APIRouter()

rag_retriver = RAGRetriever(vectorstore, embedding_manager,distance_threshold=1.5)
class AskRequest(BaseModel):
    question: str

@router.post("/ask")
def ask(req: AskRequest):
    question = req.question

    docs = rag_retriver.retrieve(query=question, top_k=5)

    if not docs:
        return {
            "question": question,
            "answer": "no relevant information found",
            "sources": []
        }

    context = "\n\n".join(f"- {doc['content']}" for doc in docs)

    prompt = f"""
You are a news summarization assistant.

RULES:
- ONLY use the provided news articles.
- Answer strictly based on the user's query topic.
- DO NOT invent information.
- DO NOT change the topic.

User Query:
{question}

News Articles:
{context}

Answer:
"""

    answer = generate_answer(prompt)

    return {
        "question": question,
        "answer": answer,
        "sources": [
            {
                "rank": doc["rank"],
                "distance": doc["distance"]
            } for doc in docs
        ]
    }
