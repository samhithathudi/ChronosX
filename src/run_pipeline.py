import os
import sys

# Configuration
TICKER = "AAPL"
QUERY = "stock market"
LANG = "en"
NEWS_LIMIT = 20

# Filenames
from datetime import datetime
timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
raw_news = f"data/news_{timestamp}.json"
cleaned_news = f"data/cleaned/cleaned_news_{timestamp}.json"
sentiment_news = f"data/sentiment/sentiment_news_{timestamp}.json"
merged_news = f"data/merged/merged_news_{TICKER.lower()}_{timestamp}.json"

# 1. Fetch news
print("Fetching news...")
os.system(f"python3 src/news_ingest.py")
# Find the newest file in data/
files = sorted([f for f in os.listdir("data") if f.startswith("news_") and f.endswith(".json")], reverse=True)
raw_news = "data/" + files[0]

# 2. Clean news
print("Cleaning news...")
os.makedirs("data/cleaned", exist_ok=True)
os.system(f"python3 src/clean_news.py {raw_news} {cleaned_news}")

# 3. Sentiment analysis
print("Analyzing sentiment...")
os.makedirs("data/sentiment", exist_ok=True)
os.system(f"python3 src/sentiment_news.py {cleaned_news} {sentiment_news}")

# 4. Merge with price
print("Merging with stock price...")
os.makedirs("data/merged", exist_ok=True)
os.system(f"python3 src/merge_sentiment_price.py {sentiment_news} {TICKER} {merged_news}")

# 5. Plot
print("Plotting sentiment vs. price...")
os.system(f"python3 src/plot_sentiment_vs_price.py {merged_news}")
