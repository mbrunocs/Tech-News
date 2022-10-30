from tech_news.database import find_news


# ref: https://stackoverflow.com/questions/1143671/
#       how-to-sort-objects-by-multiple-keys
def top_5_news():
    result = [row for row in find_news() if row["comments_count"] > 0]
    return [(row["title"], row["url"]) for row in sorted(
        result, key=lambda k: (-k['comments_count'], k['title']))][:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
