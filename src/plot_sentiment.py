import json
import matplotlib.pyplot as plt
import sys

# Usage: python3 src/plot_sentiment.py data/sentiment/sentiment_news.json

if len(sys.argv) != 2:
    print("Usage: python src/plot_sentiment.py <sentiment_json>")
    exit(1)

with open(sys.argv[1], "r") as f:
    articles = json.load(f)
polarities = [art["polarity"] for art in articles]

plt.hist(polarities, bins=20, edgecolor="black")
plt.title("Sentiment Polarity Histogram")
plt.xlabel("Polarity")
plt.ylabel("Article Count")
plt.show()
