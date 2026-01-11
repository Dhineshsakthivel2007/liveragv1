from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Live News RAG")
app.include_router(router)
