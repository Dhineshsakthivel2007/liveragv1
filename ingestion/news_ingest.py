import time
from ingestion.news_fetcher import fetch_latest_news
from rag.embeddings import embedding_manager
from rag.vectorstore import vectorstore
from langchain_text_splitters import RecursiveCharacterTextSplitter
seen_articles=set()
text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)
def articles_to_text(article):
    return f"""
    title:{article.get('title')}
    published At:{article.get('publishedAt')}
    soource:{article.get('source',{}).get('name')}
    description:{article.get('description')}
    content:{article.get('content')}"""
def ingest_latest_news():
    articles=fetch_latest_news(country='us',category='technology')
    new_texts=[]
    for article in articles:
        url=article.get("url")
        if not url or url in seen_articles:
            continue
        seen_articles.add(url)
        new_texts.append(articles_to_text(article))
    if not new_texts:
        return
    chunks=text_splitter.split_text("\n".join(new_texts))
    embeddings=embedding_manager.generate_embeddings(chunks)
    vectorstore.add_texts(chunks,embeddings)
    print(f"ingested {len(chunks)} new new chunks")
def auto_news_ingestion():
        while True:
            ingest_latest_news()
            time.sleep(300)
if __name__ == "__main__":
    print("🚀 Running manual news ingestion...")
    ingest_latest_news()
