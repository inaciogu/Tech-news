import time
import requests
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news = []

    for item in selector.css(".entry-header"):
        news_title = item.css(".entry-title a::attr(href)").get()
        news.append(news_title)

    return news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)

    next_page_link = selector.css(".next::attr(href)").get()

    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    tags = []
    news_url = ""
    first_paragraph = selector.css(".entry-content p")[0]

    # get text attributes from all nodes
    # https://stackoverflow.com/questions/33088402/extracting-text-within-em-tag-in-scrapy
    news_summary = "".join(first_paragraph.xpath(".//text()").extract())

    for link in selector.css("link"):
        if link.css("::attr(rel)").get() == "canonical":
            news_url = link.css("::attr(href)").get()

    for tag in selector.css(".post-tags a::text").getall():
        tags.append(tag)

    news_data = {
        "url": news_url,
        "title": selector.css(".entry-title::text").get(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".author a::text").get(),
        "comments_count": 0,
        "summary": news_summary,
        "tags": tags,
        "category": selector.css(".category-style .label::text").get(),
    }

    return news_data


# Requisito 5
def get_tech_news(amount):
    tech_news = []
    page_url = "https://blog.betrybe.com"

    while len(tech_news) < amount:
        page_content = fetch(page_url)
        news_urls = scrape_novidades(page_content)
        for url in news_urls:
            if len(tech_news) != amount:
                html_content = fetch(url)
                news_data = scrape_noticia(html_content)
                tech_news.append(news_data)

        page_url = scrape_next_page_link(page_content)

    create_news(tech_news)

    return tech_news
