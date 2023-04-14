import requests
import time
from parsel import Selector
import re


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


def text_formatter(text: str):
    text = text.replace(u'\xa0', u'')
    return "".join(text.strip())


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("span.author > a::text").get()
    reading_time = selector.css("li.meta-reading-time::text").get()
    converted_reading_time = reading_time.split(" ")[0]
    category = selector.css("span.label::text").get()

    title = selector.css("h1.entry-title::text").get()
    title = text_formatter(title)

    summary = selector.css("div.entry-content > p").get()
    summary = re.sub('<[^>]+?>', '', summary)
    summary = text_formatter(summary)

    return (
        {
            "url": url,
            "title": title,
            "timestamp": timestamp,
            "writer": writer,
            "reading_time": int(converted_reading_time),
            "summary": summary,
            "category": category,
        }
    )


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
