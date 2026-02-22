import feedparser
import json
from datetime import datetime

RSS_URL = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"

def fetch_news():
    feed = feedparser.parse(RSS_URL)

    news_list = []

    for entry in feed.entries[:10]:
        news = {
            "title": entry.title,
            "link": entry.link,
            "published": str(entry.published)
        }
        news_list.append(news)

    return news_listOllama


def save_news(news):
    filename = "data/news.json"

    try:
        with open(filename, "r", encoding="utf-8") as f:
            old_news = json.load(f)
    except:
        old_news = []

    old_titles = {n["title"] for n in old_news}

    new_unique_news = [
        n for n in news if n["title"] not in old_titles
    ]

    updated_news = old_news + new_unique_news

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(updated_news, f, indent=4)

    print(f"New articles found: {len(new_unique_news)}")


if __name__ == "__main__":
    news = fetch_news()
    save_news(news)

    print(f"{len(news)} news articles saved.")


    