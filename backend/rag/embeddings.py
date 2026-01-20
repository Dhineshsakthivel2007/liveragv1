import numpy as np
from sentence_transformers import SentenceTransformer
class EmbeddingManager:
    def __init__(self,model_name:str="all-MiniLM-L6-v2"):
        self.model_name=model_name
        self._load_model()
    def _load_model(self):
        try:
            print(f"model name{self.model_name}")
            self.model=SentenceTransformer(self.model_name)
            print(f"model loaded successfully model name{self.model_name}")
        except Exception as e:
            print(f"the error occuring is {e}")
            raise
    def generate_embeddings(self,texts:list[str]) ->list[list[float]]:
        if not self.model:
            raise ValueError("modelnot found")
        print(f"generate embeddings for {len(texts)} texts")
        embeddings=self.model.encode(texts,show_progress_bar=True)
        return embeddings.tolist()
embedding_manager=EmbeddingManager()