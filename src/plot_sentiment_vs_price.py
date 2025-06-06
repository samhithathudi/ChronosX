import json
import matplotlib.pyplot as plt
import sys

if len(sys.argv) != 2:
    print("Usage: python src/plot_sentiment_vs_price.py <merged_json>")
    exit(1)

with open(sys.argv[1], "r") as f:
    articles = json.load(f)

# Filter articles with both polarity and close_price
rows = [
    (a["published_at"][:10], a["polarity"], a["close_price"])
    for a in articles
    if a.get("polarity") is not None and a.get("close_price") is not None
]

# Sort by date
rows.sort()

dates = [r[0] for r in rows]
polarities = [r[1] for r in rows]
prices = [r[2] for r in rows]

fig, ax1 = plt.subplots()

color = 'tab:blue'
ax1.set_xlabel('Date')
ax1.set_ylabel('Polarity', color=color)
ax1.plot(dates, polarities, color=color, marker="o", label="Polarity")
ax1.tick_params(axis='y', labelcolor=color)
ax1.tick_params(axis='x', rotation=45)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:green'
ax2.set_ylabel('Close Price', color=color)
ax2.plot(dates, prices, color=color, marker="x", label="Close Price")
ax2.tick_params(axis='y', labelcolor=color)

plt.title('News Sentiment vs Stock Price')
fig.tight_layout()
plt.show()
