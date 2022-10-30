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


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
