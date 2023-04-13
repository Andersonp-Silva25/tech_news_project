import requests
import time


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
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
