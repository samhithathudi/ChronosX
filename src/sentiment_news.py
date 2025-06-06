import json
from textblob import TextBlob
import os

def add_sentiment(input_filepath, output_filepath):
    with open(input_filepath, "r") as fin:
        articles = json.load(fin)
    for art in articles:
        text = art.get("cleaned_text", "")
        tb = TextBlob(text)
        art["polarity"] = tb.sentiment.polarity
        art["subjectivity"] = tb.sentiment.subjectivity
    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
    with open(output_filepath, "w") as fout:
        json.dump(articles, fout, indent=2)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python src/sentiment_news.py <input_cleaned_json> <output_json>")
        exit(1)
    add_sentiment(sys.argv[1], sys.argv[2])
    print(f"Sentiment scores written to {sys.argv[2]}")
