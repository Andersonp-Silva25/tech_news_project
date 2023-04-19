from tech_news.database import find_news
from collections import Counter


def get_categories(list_news):
    all_categories = []
    for new in list_news:
        all_categories.append(new["category"])
    return sorted(all_categories)


def most_common_counter(list, limit):
    counter = Counter(list)
    return counter.most_common(limit)


# Requisito 10
def top_5_categories():
    list_news = find_news()
    all_categories = get_categories(list_news)
    most_common_categories = most_common_counter(all_categories, 5)
    top_5_list = [category[0] for category in most_common_categories]
    return top_5_list
