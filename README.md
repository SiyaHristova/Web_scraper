# Web Scraper

## Summary

Team task to do in collaboration under the supervision and guidance of mentor appointed from Strypes.

The task is to develop web scraper for scraping blog posts, store the data, to manipulate the data(search, sort, etc) and then present it using front-end.

The scraping and managing the data should be created using TDD as approach.

## Project's directories structure:

```
Full_Monty
├── frontend
│   ├── app
│   │   ├── img_url.json
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── static
│   │   │   ├── css
│   │   │   │   └── styles.css
│   │   │   └── img
│   │   │       └── floral-dark-trans-o.png
│   │   ├── temp_files
│   │   │   ├── data.json
│   │   │   └── raw-data.txt
│   │   ├── templates
│   │   │   ├── 404.html
│   │   │   ├── about-us.html
│   │   │   ├── base.html
│   │   │   ├── index.html
│   │   │   └── post.html
│   │   └── the_data.json
│   └── microblog.py
├── github-clones-shot.png
├── main.py
├── module
│   ├── __init__.py
│   ├── post.py
│   ├── post_scraper.py
│   └── url_scraper.py
├── QUESTIONS.md
├── README.md
├── requirements.txt
└── test
    ├── conftest.py
    ├── test_integration.py
    └── unit_tests
        ├── test_post.py
        ├── test_post_scraper.py
        └── test_url_scraper.py

10 directories, 28 files
```
