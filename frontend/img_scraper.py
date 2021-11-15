from bs4 import BeautifulSoup
import requests
import json

class ImgScraper():

    BLOG_URL = 'https://www.kulinarno-joana.com/'
    IMGS_TO_SCRAPE = 20
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

    def get_twenty_urls() -> list:
        """
        Iterates through the pages until certain number of post urls is scraped

        Returns:
            list: Sliced list of post urls
        """
        urls = []
        page_number = 1
        while len(urls) < ImgScraper.IMGS_TO_SCRAPE: 
            page_url = ImgScraper.BLOG_URL + f"page/{page_number}/"
            urls.extend(ImgScraper._get_post_urls(page_url))
            page_number += 1
        return urls[0:ImgScraper.IMGS_TO_SCRAPE]

    def get_twenty_images(urls_list) -> list:
        """Scrapes the first image of each article

        Args:
            urls_list (list): list of article urls

        Returns:
            list: list of image urls
        """
        image_urls = []

        for url in urls_list:
            article = requests.get(url)
            soup = BeautifulSoup(article.text, features='html.parser')
            image = soup.find('img')['src']
            image_urls.append(image)

        return image_urls

    @staticmethod
    def print_to_json(filename, image_urls):
        """Prints image urls to json file as an array

        Args:
            filename (string): name of json file
            image_urls (list): list of image urls
        """

        if not filename.endswith(".json"):
            filename += ".json"

        with open(filename, 'w', encoding= 'utf8') as file:
            file.write(json.dumps(image_urls, indent=4, ensure_ascii=False))
        

if __name__ == '__main__':

    twenty_posts = ImgScraper.get_twenty_urls()
    image_scraper = ImgScraper.get_twenty_images(twenty_posts)
    ImgScraper.print_to_json('img_url', image_scraper)