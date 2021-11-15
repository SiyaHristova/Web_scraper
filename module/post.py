import json
from collections import Counter

class Post():
    
    WORD_LIST_LEN = 3
    MIN_WORD_LEN = 3
    PARAGRAPHS_LEN = 3

    def __init__(self, title, date, text, comments=None, first_paragraphs=None) -> None:
        """
        A class to manage the data within the post 

        Args:
            title (str): post title
            date (str): post date
            text (str): article content
            comments (list): list of comments, organized as tuples (author, comment). Defaults to None.
            first_paragraphs (list): list of article paragraphs, stored as strings. Defaults to None.
        """
        self.title = title
        self.date = date
        self.text : str = text
        self.comments = comments
        self.paragraphs = first_paragraphs[0:Post.PARAGRAPHS_LEN]
    
    def _get_most_common_words(self, word_list):
        """
        Filters out the most commonly used words 

        Args:
            word_list (str): body of the article

        Returns:
            dict: dictioanry with {word: occurence} of certain number of keywords
        """
        dict_to_return = {}
        words_to_count = (word for word in word_list if len(word) > Post.MIN_WORD_LEN)
        word_counter = Counter(words_to_count)
        words = word_counter.most_common(Post.WORD_LIST_LEN)
        
        for word in words:
            dict_to_return[word[0]] = word[1]

        return dict_to_return

    def get_as_json_object(self):
        """
        json formater

        Returns:
            str: post data, organized as json object
        """
        return {"title_1" : self.title,
                "date_of_publishing": self.date, 
                "content":self.paragraphs, 
                "most_used_words" : self._get_most_common_words(self.text),
                "comments":self.comments}

    def print_to_text_file(self, filename) -> None:
        """
        Adds post data to .txt file

        Args:
            filename (str): name of file to be created
        """
        with open(filename, 'a+') as f:
            f.write(self.title + '\n')
            f.write(self.date + '\n')
            f.write(self.text + '\n')
            f.write((20 * '-') + '\n')
    
    @staticmethod
    def print_to_json_file(posts_list, filename):
        """
        Adds post data to .json file

        Args:
            posts_list (list): list of posts, organized as json objects
            filename (str): name of file to be created
        """
        if not filename.endswith(".json"):
            filename += ".json"
        
        with open(filename, 'w', encoding= 'utf8') as file:
            file.write(json.dumps(posts_list, indent=4, ensure_ascii=False))