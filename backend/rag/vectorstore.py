import os
import uuid
import chromadb
import numpy as np
from typing import Any
class VectoreStore:
    def __init__(self,collection_name:str="rag_documents",persist_directory:str=r"backend\vectorStore"):
        self.collection_name=collection_name
        self.persist_directory=persist_directory
        self.client=None
        self.collection=None
        self._initialize_store()
    def _initialize_store(self):
        try:
            os.makedirs(self.persist_directory,exist_ok=True)
            self.client=chromadb.PersistentClient(path=self.persist_directory)
            self.collection=self.client.get_or_create_collection(name=self.collection_name,metadata={"description":"Document for rag"})
            print(f"vector store initialized{self.collection_name}")
            print(f"exsisting_documents{self.collection.count()}")
        except Exception as e:
            print(f"error is {e}")
            raise
    def add_documents(self,documents:list[Any],embeddings:list[list[float]]):
        ids,metadatas,texts=[],[],[]
        for i,(doc,embedding) in enumerate(zip(documents,embeddings)):
            ids.append(f"doc_{uuid.uuid4().hex[:8]}_{i}")
            texts.append(doc.page_content)
            metadata=dict(doc.metadata)
            metadata['doc_index']=i
            metadata["content_length"]=len(doc.page_content)[0]
            metadatas.append(metadata)
        self.collection.add(ids=ids,documents=texts,embeddings=embeddings,metadatas=metadatas)

    def add_texts(self, texts: list[str], embeddings: list[list[float]], metadatas=None):
        ids = []
        final_metadatas = []

        for i, text in enumerate(texts):
            ids.append(f"news_{uuid.uuid4().hex[:8]}_{i}")
            final_metadatas.append(metadatas[i] if metadatas else {"source": "news"})

        self.collection.add(
            ids=ids,
            documents=texts,
            embeddings=embeddings,
            metadatas=final_metadatas
        )

        print(f"📰 Added {len(texts)} news texts")
vectorstore=VectoreStore()