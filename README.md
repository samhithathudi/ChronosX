# ChronosX: Quant News Sentiment Research Pipeline

ChronosX is an end-to-end automated research pipeline for analyzing the effect of news on the stock market.

## Features

- Fetches news headlines from the web
- Cleans and analyzes sentiment using NLP
- Merges news data with real stock prices
- Visualizes the relationship between sentiment and price movements

## How to Run

```bash
# Clone the repo
git clone https://github.com/samhithathudi/ChronosX.git
cd ChronosX

# Create and activate a Python virtual environment (Python 3.12+ recommended)
python3.12 -m venv venv
source venv/bin/activate

# Install all dependencies
pip install -r requirements.txt

# Download NLP datasets (required only once)
python3
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('stopwords')
>>> nltk.download('wordnet')
>>> exit()
python3 -m textblob.download_corpora

# Run the pipeline!
python3 src/run_pipeline.py

