from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_news_source, get_articles
from ..models import NewsSource 

#views
@main.route('/')
def index():
    """view root page function that returns the index page and its data
    """
    technology = get_news_source('technology')
    business = get_news_source('business')
    entertainment = get_news_source('entertainment')
    title = 'All cap'

    return render_template('index.html', title = title, technology = technology, business = business, entertainment = entertainment)

@main.route('/news_articles/<id>')
def articles(id):
    """
    veiw articles page function that returns the article page its data
    """
    articles = get_articles(id)
    title = f'All cap | {id}'

    return render_template('news_articles.html', title = title, articles = articles)
