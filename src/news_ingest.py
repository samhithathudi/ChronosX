from newsapi import NewsApiClient
import json
import os
from datetime import datetime

# 1. Load your API key from the environment variable
NEWS_API_KEY = os.getenv("NEWSAPI_KEY")
if not NEWS_API_KEY:
    raise RuntimeError("Set environment variable NEWSAPI_KEY with your NewsAPI key")

# 2. Initialize the NewsApiClient
newsapi = NewsApiClient(api_key=NEWS_API_KEY)

def fetch_top_headlines(query="stock market", language="en", page_size=20):
    """
    Fetches the latest top headlines matching `query`.
    Returns a list of article dictionaries.
    """
    response = newsapi.get_top_headlines(q=query, language=language, page_size=page_size)
    articles = response.get("articles", [])
    return articles

if __name__ == "__main__":
    # 3. Call the function and save results to a timestamped JSON file
    articles = fetch_top_headlines()
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    output_dir = "data"
    os.makedirs(output_dir, exist_ok=True)       # create data/ if it doesn’t exist
    output_path = f"{output_dir}/news_{timestamp}.json"
    with open(output_path, "w") as f:
        json.dump(articles, f, indent=2)
    print(f"Saved {len(articles)} articles to {output_path}")
