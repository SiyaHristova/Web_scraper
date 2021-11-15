import requests 
from bs4 import BeautifulSoup

class UrlScraper():

    BLOG_URL = 'https://www.kulinarno-joana.com/'
    POSTS_TO_SCRAPE = 20
    def __init__(self):
        pass

    def _get_post_urls(page_url) -> list:
        """
        Scrapes post urls from the index pages and stores them in a list

        Args:
            page_url (str): The url of the blog we are going to scrape

        Returns:
            list: List of post urls
        """
        r = requests.get(page_url)
        soup = BeautifulSoup(r.text, features='html.parser')
        articles = soup.find_all("article")
        url_list = []
        for article in articles:
            url_list.append(article.find('h2', class_='entry-title').a['href'])

        return url_list

    def get_twenty_posts() -> list:
        """
        Iterates through the pages until certain number of post url is scraped

        Returns:
            list: Sliced list of post urls
        """
        urls = []
        page_number = 1
        while len(urls) < UrlScraper.POSTS_TO_SCRAPE: 
            page_url = UrlScraper.BLOG_URL + f"page/{page_number}/"
            urls.extend(UrlScraper._get_post_urls(page_url))
            page_number += 1
        return urls[0:UrlScraper.POSTS_TO_SCRAPE]