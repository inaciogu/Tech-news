import re
from datetime import datetime
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
    try:
        datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Data inválida")

    months = {
        "01": "janeiro",
        "02": "fevereiro",
        "03": "março",
        "04": "abril",
        "05": "maio",
        "06": "junho",
        "07": "julho",
        "08": "agosto",
        "09": "setembro",
        "10": "outubro",
        "11": "novembro",
        "12": "dezembro",
    }

    splitted = date.split("-")

    formatted = f"{int(splitted[2])} de {months[splitted[1]]} de {splitted[0]}"

    news = search_news({"timestamp": formatted})
    formatted_news = []

    for item in news:
        tuple_news = (item["title"], item["url"])
        formatted_news.append(tuple_news)

    return formatted_news


# Requisito 8
def search_by_tag(tag):
    news = search_news({'tags': {"$in": [re.compile(tag, re.IGNORECASE)]}})
    formatted_news = []

    for item in news:
        tuple_news = (item["title"], item["url"])
        formatted_news.append(tuple_news)

    return formatted_news


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
