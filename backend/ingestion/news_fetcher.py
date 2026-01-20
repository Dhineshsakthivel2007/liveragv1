import requests,os
from datetime import datetime,timedelta
from dotenv import load_dotenv
load_dotenv()
news_api_key=os.getenv("NEWS_API_KEY")
base_url="https://newsapi.org/v2/top-headlines"
def fetch_latest_news(language="en",country=None,category=None,page_size=20):
    params={
        "apiKey":news_api_key,
        "language":language,
        "pageSize":page_size
    }
    if country:
        params["country"]=country
    if category:
        params["category"]=category
    try:
        response=requests.get(base_url,params=params,timeout=10)
        response.raise_for_status()
        data=response.json()
        if data.get("status")!="ok":
            print("api error",data)
            return[]
        return data.get("articles",[])
    except Exception as e:
        print(f"error in fetching{e}")
        return []
# if __name__ == "__main__":
#     articles = fetch_latest_news(country="us")

#     print(f"Fetched {len(articles)} articles")
#     for a in articles[:3]:
#         print("-", a["title"])
