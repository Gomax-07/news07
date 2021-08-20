import urllib.request, json
from .models import Category, NewsSource, NewsArticle
from datetime import date

#getting the Api key
api_key = 'c4371e55575b4ec2a980a1c7bb9c16dc'

#getting the news base url
base_url = None

#getting the article url
articles = None

def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['SOURCE_BASE_URL']
    articles_url = app.config['ARTICLE_BASE_URL']

def get_news_source(category):
    """function that gets the json response tot oururl request
    """
    get_news_source_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_source_url) as url:
        get_news_source_data = url.read()
        get_news_source_response = json.loads(get_news_source_data)

        news_source_results = None

        if get_news_source_response['sources']:
            news_source_results_list = get_news_source_response['sources']
            news_source_results = process_news_source(news_source_results_list)
      
    return news_source_results

def process_news_source(news_source_list):
    """function that process the news source results and turns tem into a of objects
    
    Args:
       news_source_list: A list of dictionaires that contain source details

    Returns:
       news_source_results:A list of source objects
    """
    news_source_results = []

    for news_source_item in news_source_list:
        id = news_source_item.get('id')
        name = news_source_item.get('name')
        description = news_source_item.get('description')
        url = news_source_item.get('url')     

        news_source_object = NewsSource(id, name, description, url)
        news_source_results.append(news_source_object)

    return news_source_results

def get_articles(id):
    """function that process the articles and a list of articles objects
    """
    get_articles_url = articles_url.format(id, api_key)  

    with urllib.request.urlopen(get_articles_url) as url:
        news_article_results = json.loads(url.read())  

        news_article_object = None
        if news_article_results['articles']:
            news_article_object = process_news_source(news_article_results['articles']) 

    return news_article_object

def get_news_source(category):    
    """function that gets the json response to our url request
    """
    get_news_source_url = base_url.format(category, 'c4371e55575b4ec2a980a1c7bb9c16dc')
    with urllib.request.urlopen(get_news_source_url) as url:
        get_news_source_data = url.read()
        get_news_source_response = json.loads(get_news_source_data)

        news_source_results = None

        if get_news_source_response['sources']:
            news_source_results_list = get_news_source_response['sources']
            news_source_results = process_news_source(news_source_results_list)
            
    return news_source_results
