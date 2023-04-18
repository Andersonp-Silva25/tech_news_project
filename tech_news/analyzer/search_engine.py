from tech_news.database import search_news
import re
from datetime import datetime


def ignore_sensitive_case(title):
    return re.compile(title, re.I)


def create_formatted_news_list(array):
    news_list = []
    for news in array:
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
    try:
        new_date = datetime.strptime(date, "%Y-%m-%d")
        converted_date = new_date.strftime("%d/%m/%Y")
        get_news = search_news({"timestamp": converted_date})
        return create_formatted_news_list(get_news)
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
