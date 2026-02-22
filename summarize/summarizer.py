import json
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def summarize_text(text):

    prompt = f"""
Summarize this news headline for Instagram post.

Rules:
- Maximum 2 lines
- News tone
- Simple English
- Add one emoji

News:
{text}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    return result["response"].strip()


def summarize_news():

    with open("data/news.json", "r", encoding="utf-8") as f:
        news = json.load(f)

    summarized = []

    for item in news[:5]:
        summary = summarize_text(item["title"])

        summarized.append({
            "title": item["title"],
            "summary": summary
        })

        print("✔ Summarized:", item["title"])

    with open("data/summarized_news.json", "w", encoding="utf-8") as f:
        json.dump(summarized, f, indent=4)


if __name__ == "__main__":
    summarize_news()