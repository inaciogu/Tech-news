import re
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news = search_news({"title": re.compile(title, re.IGNORECASE)})
    formatted_news = []

    for item in news:
        tuple_news = (item["title"], item["url"])
        formatted_news.append(tuple_news)

    return formatted_news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
