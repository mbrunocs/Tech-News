import requests
import time
import parsel
from tech_news.database import create_news


def fetch(url, timeout=3):
    time.sleep(1)
    try:
        response = requests.get(
            url, timeout=timeout, headers={"user-agent": "Fake user-agent"})
        response.raise_for_status()
        return response.text
    except (requests.HTTPError, requests.ReadTimeout):
        return None


def scrape_novidades(html_content: str):
    selector = parsel.Selector(html_content)
    links = selector.css("h2.entry-title a::attr(href)").getall()
    return links


def scrape_next_page_link(html_content: str):
    selector = parsel.Selector(html_content)
    return selector.css("a.next ::attr(href)").get()


# Ref:  https://devpress.csdn.net/python/62f50311c6770329307fafd1.html
#       https://www.w3schools.com/CSSref/sel_nth-of-type.php
def scrape_noticia(html_content: str):
    selector = parsel.Selector(html_content)
    return dict({
        "url": selector.css("head link[rel=canonical]::attr(href)").get(),
        "title": selector.css("h1.entry-title ::text").get().strip(),
        "timestamp": selector.css("li.meta-date ::text").get(),
        "writer": selector.css("span.author a::text").get(),
        "comments_count": selector.css("comment").getall().__len__(),
        "summary":
            ''.join(selector
                .css("div.entry-content > p:nth-of-type(1) *::text")
                .getall()).strip(),
        "tags": selector.css("a[rel=tag]::text").getall(),
        "category": selector.css("span.label ::text").get(),
    })


def get_tech_news(amount):
    page = fetch("https://blog.betrybe.com/")
    news = []
    while len(news) < amount:
        for news_link in scrape_novidades(page)[:(amount - len(news))]:
            news.append(scrape_noticia(fetch(news_link)))
        if not len(news) == amount:
            page = fetch(scrape_next_page_link(page))
    create_news(news)
    return news
