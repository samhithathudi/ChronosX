import json
import yfinance as yf
from datetime import datetime
import os

def load_sentiment(filename):
    with open(filename, "r") as f:
        return json.load(f)

def fetch_stock_history(ticker, start, end):
    df = yf.download(ticker, start=start, end=end, progress=False)
    return df

def main(sentiment_file, ticker, output_file):
    articles = load_sentiment(sentiment_file)
    # Pick date range
    dates = [art["published_at"][:10] for art in articles if "published_at" in art]
    start_date = min(dates)
    end_date = max(dates)
    # Download prices
    df = fetch_stock_history(ticker, start=start_date, end=end_date)
    df = df.reset_index()
    df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")
    # Attach close price to each article
    for art in articles:
        pub_date = art.get("published_at", "")[:10]
        match = df[df["Date"] == pub_date]
        art["close_price"] = float(match["Close"].values[0]) if not match.empty else None
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as f:
        json.dump(articles, f, indent=2)
    print(f"Merged sentiment with stock price for {ticker} written to {output_file}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python src/merge_sentiment_price.py <sentiment_json> <stock_ticker> <output_json>")
        exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
