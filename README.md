🧠 Live News RAG Application (RSS-Based)

A Live Retrieval-Augmented Generation (RAG) application that fetches real-time news from RSS feeds, converts them into embeddings, stores them in a vector database, and generates grounded, source-aware answers using a Large Language Model (LLM).

This project demonstrates how modern AI systems like news assistants and search-based chatbots work internally.

🚀 Features

🔴 Live data ingestion using RSS feeds (no API keys required)

📰 Real-time news updates

🧠 Semantic search using vector embeddings

📦 Vector database for efficient retrieval

🤖 LLM-powered answers with source references

❌ No static dataset – always fresh data

🏗️ Architecture
RSS Feeds
   ↓
Feed Parser
   ↓
Text Cleaning & Chunking
   ↓
Embedding Model
   ↓
Vector Database
   ↓
Retriever
   ↓
LLM Response (with sources)

🛠️ Tech Stack

Programming Language: Python

Data Source: RSS Feeds (BBC, Google News, etc.)

Feed Parsing: feedparser

Embeddings: Sentence Transformers (all-MiniLM-L6-v2)

Vector Database: ChromaDB

LLM: OpenAI / local LLM (configurable)

Framework (optional): Streamlit / FastAPI

📦 Installation
1️⃣ Clone the repository
git clone https://github.com/your-username/live-rag-news.git
cd live-rag-news

2️⃣ Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

🔗 RSS Feed Sources

Example feeds used:

BBC News

https://feeds.bbci.co.uk/news/rss.xml


Google News (India)

https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en


You can easily add more feeds in the configuration file.

▶️ How It Works

Fetches latest articles from RSS feeds

Cleans and combines title + summary

Converts text into embeddings

Stores embeddings in a vector database

On user query:

Retrieves relevant news chunks

Passes context to the LLM

Generates an answer with sources

🧪 Example Query

User:

What are today’s top technology headlines?

System:

Retrieves latest tech news

Generates summarized answer

Includes article links as references

📌 Why RSS Instead of APIs?

✅ No rate limits

✅ No API keys

✅ Free & reliable

✅ Officially supported by news providers

✅ Ideal for real-time AI systems

📈 Future Improvements

Voice command integration

Full article extraction

Scheduled embedding updates

Multi-language support

UI improvements

Hybrid RSS + REST API ingestion

🧑‍💻 Author

Dhinesh
AI & Data Science Student
Interested in RAG systems, LLMs, and real-world AI applications