🧠 Live News RAG Application (API-Based)

A Live Retrieval-Augmented Generation (RAG) application that fetches real-time news using APIs, converts articles into vector embeddings, stores them in a vector database, and generates grounded, source-aware answers using the Grok Large Language Model (LLM).

This project demonstrates how modern AI systems such as Perplexity-style news assistants and search-based chatbots operate internally.

🚀 Features

🟢 Live news ingestion using News APIs
📰 Real-time news updates (always fresh data)
🧠 Semantic search using vector embeddings
📦 Vector database for efficient similarity retrieval
🤖 LLM-powered answers using Grok LLM
🔗 Source-aware responses with article references
❌ No static dataset

🏗️ Architecture
News API
   ↓
API Data Fetcher
   ↓
Text Cleaning & Chunking
   ↓
Embedding Model
   ↓
Vector Database
   ↓
Retriever
   ↓
Grok LLM Response (with sources)

🛠️ Tech Stack

Programming Language: Python

Data Source: News APIs (configurable)

Data Fetching: REST API requests

Embeddings: Sentence Transformers (all-MiniLM-L6-v2)

Vector Database: ChromaDB

LLM: Grok LLM

Framework (optional): Streamlit / FastAPI

▶️ How It Works

Fetches the latest news articles via APIs

Cleans and combines title + description + content

Splits text into chunks

Converts chunks into vector embeddings

Stores embeddings in ChromaDB

On user query:

Retrieves the most relevant news chunks

Sends context to Grok LLM

Generates a fact-grounded answer with sources

🧪 Example Query

User:

What are today’s top technology headlines?

System:

Retrieves latest technology news via API

Performs semantic search

Generates a summarized response

Includes article URLs as references

📌 Why News APIs Instead of RSS?

✅ More structured data
✅ Better filtering (category, language, country)
✅ Reliable metadata (author, publish time, source)
✅ Suitable for scalable production systems
✅ Industry-standard for real-time applications

📈 Future Improvements

Voice-based news queries

Full article scraping and summarization

Scheduled background embedding updates

Multi-language news support

Improved UI/UX

Hybrid API + Web scraping pipeline

🧑‍💻 Author

Dhinesh
AI & Data Science Student
Interested in RAG systems, LLMs, and real-world AI applications