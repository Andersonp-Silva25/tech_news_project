from tech_news.database import search_news
import re


def ignore_sensitive_case(title):
    return re.compile(title, re.I)


def create_formatted_news_list(list_news_by_title):
    news_list = []
    for news in list_news_by_title:
        news = (news["title"], news["url"])
        news_list.append(news)
    return news_list


# Requisito 7
def search_by_title(title):
    modificated_title = ignore_sensitive_case(title)
    get_news_by_title = search_news({"title": modificated_title})
    return create_formatted_news_list(get_news_by_title)


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
