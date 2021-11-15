import requests 
from bs4 import BeautifulSoup

from module.post import Post

class PostScraper():

    def __init__(self, post_urls):
        """
        A class responsible for scraping each post

        Args:
            post_urls (list): A list of certain post urls, which are going to be scraped
        """
        self.post_urls = post_urls

    def get_last_posts(self) -> list:
        """
        Calls the scraping of each individual post in the url list

        Returns:
            list: A list of Post objects
        """
        posts = []

        for url in self.post_urls:
            posts.append(self._read_post(url))
        
        return posts
    
    def _read_post(self, url_post) -> Post:
        """
        Reads certain content of the post and returns it divided into arguments of an instance of class Post

        Args:
            url_post (str): A string of the post's url

        Returns:
            Post: Instance of class Post
        """
        r = requests.get(url_post)

        soup = BeautifulSoup(r.text, features='html.parser')

        post = soup.find('article')
        title = post.find('h1', class_='entry-title').text
        date = post.find('span', class_='posted-on').time['title']
        body = post.find('div', class_='entry-content')
        paragraphs = self._get_paragraphs(body)

        comments_soup = soup.find('ol', class_='comment-list')
        
        comments = None if comments_soup is None else self._get_comments(comments_soup) 

        text = self._remove_linked_posts(body)

        return Post(title, date, text, comments=comments, first_paragraphs=paragraphs)

    def _get_paragraphs(self, body):
        """
        Filters only the text from all html subtags of the post by iterating through each one of them

        Args:
            body (bs4.element.Tag): The whole body of the article

        Returns:
            list: A list of all paragraphs in the article
        """
        paragraphs = []

        for paragraph in body.find_all('p'):
            self._remove_images(paragraph)
            paragraph_text = paragraph.text
            if len(paragraph_text) > 0:
                paragraphs.append(paragraph_text)

        return paragraphs

    def _remove_images(self, paragraph):
        """
        Decomposes the html paragraph tag if it contains an image

        Args:
            paragraph (bs4.element.Tag): Tag holding a paragraph 
        """
        for photo in paragraph.findChildren('img'):
            photo.decompose()

    def _get_comments(self, comments_soup) -> list:
        """
        Filters out the comment authors and comment contents and returns them as a list of tuples

        Args:
            comments_soup (bs4.element.Tag): Tag holding all the comments in the post

        Returns:
            list: List of tuples - (author, comment)
        """

        comments_list = []
        for li in comments_soup.find_all('li'):
            comment_text = li.find('div', class_='comment-content').text
            comment_author = self._remove_children(li.find('footer', class_='comment-meta'))
            comments_list.append((comment_author, comment_text))

        return comments_list

    def _remove_children(self, comment_author) -> str:
        """
        Removes all the subtags of a given element

        Args:
            comment_author (bs4.element.Tag): Tag holding the comment author info

        Returns:
            str: Name of comment author
        """
        for child in comment_author.findChildren():
            child.decompose()
        return comment_author.text.strip()

    def _remove_linked_posts(self, body) -> str:
        """
        Removes linked urls from the article body

        Args:
            body (bs4.element.Tag): The whole body of the article

        Returns:
            str: Article content with paragraphs divided by new lines
        """

        selects = body.find_all("ul", {"id": "klnArticleRelatedPosts"})
        for match in selects:
            match.decompose()

        text = ""
        for tag in body:
            text += tag.text + '\n'

        return text