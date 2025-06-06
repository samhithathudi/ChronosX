import json
import os
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Load NLTK resources
STOPWORDS = set(stopwords.words("english"))
LEMMATIZER = WordNetLemmatizer()

def clean_text(raw_html):
    # 1. Remove HTML
    text = BeautifulSoup(raw_html, "html.parser").get_text()
    # 2. Lowercase
    text = text.lower()
    # 3. Tokenize
    tokens = word_tokenize(text)
    # 4. Keep alphabetic tokens & drop stopwords
    tokens = [t for t in tokens if t.isalpha() and t not in STOPWORDS]
    # 5. Lemmatize
    tokens = [LEMMATIZER.lemmatize(t) for t in tokens]
    return " ".join(tokens)

def process_news_file(input_filepath, output_filepath):
    with open(input_filepath, "r") as fin:
        articles = json.load(fin)

    cleaned_list = []
    for art in articles:
        title = art.get("title", "")
        desc = art.get("description", "")
        content = art.get("content", "")
        # Ensure all are strings!
        combined = " ".join([
            title if isinstance(title, str) else "",
            desc if isinstance(desc, str) else "",
            content if isinstance(content, str) else ""
        ])
        cleaned_text = clean_text(combined)
        cleaned_list.append({
            "url": art.get("url"),
            "published_at": art.get("publishedAt"),
            "cleaned_text": cleaned_text
        })

    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
    with open(output_filepath, "w") as fout:
        json.dump(cleaned_list, fout, indent=2)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python src/clean_news.py <input_json> <output_json>")
        exit(1)
    process_news_file(sys.argv[1], sys.argv[2])
    print(f"Cleaned news written to {sys.argv[2]}")
