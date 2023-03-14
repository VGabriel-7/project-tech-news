from parsel import Selector
from bs4 import BeautifulSoup
import requests
import time


# Requisito 1
def fetch(url):
    try:
        print(f'Scraping on url: {url}')
        time.sleep(1)
        response = requests.get(
            url,
            timeout=3,
            headers={"user-agent": "Fake user-agent"}
        )
        if response.status_code != 200:
            return None
        return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    return selector.css('h2 a::attr(href)').getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css('nav .next::attr(href)').get()


# Requisito 4
def scrape_news(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    url = soup.find('link', {"rel": "canonical"})["href"]
    title = soup.find(class_='entry-title').text
    timestamp = soup.find(class_='meta-date').text[:10]
    writer = soup.find(class_='author').find('a').text
    reading_time = int(soup.find(class_='meta-reading-time').text[:2])
    summary = soup.find(class_='entry-content').find('p').text
    category = soup.find(class_='category-style').find(class_='label').text

    return {
        "url": url,
        "title": title.rstrip(),
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary.rstrip(),
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
