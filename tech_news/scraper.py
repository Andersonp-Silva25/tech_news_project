import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    fake_user_agent = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, headers=fake_user_agent)
        time.sleep(1)
        if (response.status_code == 200):
            return response.text
    except (requests.HTTPError, requests.ReadTimeout):
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    news = []
    for new in selector.css("div.cs-overlay"):
        news.append(new.css("a.cs-overlay-link::attr(href)").get())
    return news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css("a.next::attr(href)").get()
    if (next_page == ""):
        return None
    return next_page


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
