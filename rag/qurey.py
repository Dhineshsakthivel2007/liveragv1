from rag.vectorstore import VectoreStore
from rag.embeddings import EmbeddingManager
from typing import List, Dict, Any


class RAGRetriever:
    def __init__(self, vector_store: VectoreStore, embedding_manager: EmbeddingManager):
        self.vector_store = vector_store
        self.embedding_manager = embedding_manager

    def retrieve(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        print(f"retrieve documents for query: {query}")

        query_embedding = self.embedding_manager.generate_embeddings([query])[0]

        results = self.vector_store.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        print("Distances:", results["distances"])

        retrieved_docs = []

        if results["documents"] and results["documents"][0]:
            for i, (doc_id, document, metadata, distance) in enumerate(
                zip(
                    results["ids"][0],
                    results["documents"][0],
                    results["metadatas"][0],
                    results["distances"][0],
                )
            ):
                retrieved_docs.append({
                    "id": doc_id,
                    "content": document,
                    "metadata": metadata,
                    "distance": distance,
                    "rank": i + 1
                })

        print(f"retrieved: {len(retrieved_docs)} documents")
        return retrieved_docs