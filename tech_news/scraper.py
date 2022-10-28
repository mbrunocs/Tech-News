import requests
import time
import parsel


# Requisito 1
def fetch(url, timeout=3):
    time.sleep(1)
    try:
        response = requests.get(
            url, timeout=timeout, headers={"user-agent": "Fake user-agent"})
        response.raise_for_status()
        return response.text
    except (requests.HTTPError, requests.ReadTimeout):
        return None


# Requisito 2
def scrape_novidades(html_content: str):
    selector = parsel.Selector(html_content)
    links = selector.css("h2.entry-title a::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    return selector.css("a.next ::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
