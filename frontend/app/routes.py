from app import app
from flask import render_template
import json
from werkzeug.exceptions import abort

@app.route('/')
@app.route('/index')

def index():
    """
    index [summary]

    function for generating the index page

    Returns:
        [type]: [description]
    """

    user = {'username': 'Ангел'}

    f = open('app/data/the_data.json', 'r')

    articles = json.load(f)

    data = open('app/data/img_url.json', 'r')

    f.close()

    imgs = json.load(data)['articles']

    data.close()

    return render_template('index.html', title='Home', user=user, articles=articles, imgs=imgs)


def get_post(post_id):

    """
     [summary]

    Returns:
        [type]: [description]
    """

    f = open('app/data/the_data.json', 'r')

    articles = json.load(f)

    f.close()

    post = articles[post_id]

    if post_id > 19:
        abort(404)

    return post

@app.route('/<int:post_id>')
def post(post_id):

    """
     [summary]

    Returns:
        [type]: [description]

    """

    title = 'Рецепта'
    post = get_post(post_id)

    return render_template('post.html', title=title, post=post)


@app.route('/about')
def about_us():

    """
     [summary]

    Returns:
        [type]: [description]
    """

    us = ['Сияна', 'Калина', 'Димитър', 'Венци']

    return render_template('about-us.html', title='About', us=us)

@app.route('/page-2')
def page2():

    """
     [summary]

    Returns:
        [type]: [description]
    """
    user = {'username': 'Ангел'}

    f = open('app/data/the_data.json', 'r')

    articles = json.load(f)[5:10]

    data = open('app/data/img_url.json', 'r')

    f.close()

    imgs = json.load(data)['articles'][5:10]

    data.close()

    return render_template('index.html', title='Страница 2', user=user, articles=articles, imgs=imgs)

@app.route('/page-3')
def page3():

    """
     [summary]

    Returns:
        [type]: [description]
    """

    user = {'username': 'Ангел'}

    f = open('app/data/the_data.json', 'r')

    articles = json.load(f)[10:15]

    data = open('app/data/img_url.json', 'r')

    f.close()

    imgs = json.load(data)['articles'][10:15]

    data.close()

    return render_template('index.html', title='Страница 3', user=user, articles=articles, imgs=imgs)

@app.route('/page-4')
def page4():

    """
     [summary]

    Returns:
        [type]: [description]
    """

    user = {'username': 'Ангел'}

    f = open('app/data/the_data.json', 'r')

    articles = json.load(f)[15:20]

    data = open('app/data/img_url.json', 'r')

    f.close()

    imgs = json.load(data)['articles'][15:20]

    data.close()

    return render_template('index.html', title='Страница 4', user=user, articles=articles, imgs=imgs)