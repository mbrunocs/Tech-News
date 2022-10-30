from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    results = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(row["title"], row["url"]) for row in results]


def search_by_date(date):
    news = []
    try:
        date_f = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        results = search_news(
            {"timestamp": {"$regex": date_f, "$options": "i"}})
        for row in results:
            news.append((row["title"], row["url"]))
        return news
    except ValueError:
        raise ValueError("Data inválida")


def search_by_tag(tag):
    results = search_news({"tags": {"$regex": tag, "$options": "i"}})
    return [(row["title"], row["url"]) for row in results]


def search_by_category(category):
    results = search_news({"category": {"$regex": category, "$options": "i"}})
    return [(row["title"], row["url"]) for row in results]
