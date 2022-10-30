from tech_news.database import search_news


def search_by_title(title):
    results = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(row["title"], row["url"]) for row in results]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
