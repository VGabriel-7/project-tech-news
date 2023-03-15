from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    news_searching = search_news(
        {
            "title": {"$regex": title, "$options": "i"},
        }
    )

    return [(news["title"], news["url"]) for news in news_searching]


# Requisito 8
def search_by_date(date):
    """Seu código aqui"""


# Requisito 9
def search_by_category(category):
    news_searching = search_news(
        {
            "category": {"$regex": category, "$options": "i"},
        }
    )

    return [(news["title"], news["url"]) for news in news_searching]
