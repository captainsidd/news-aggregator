import os
import json
import random
import requests
from datetime import datetime, timedelta

# General sources from News API (ignores entertainment + sports + science, etc)
sources = 'ABC News, Al Jazeera English, Associated Press, Axios, Breitbart News, CBS News, CNN, Fox News, Google News, MSNBC, NBC News, Newsweek, New York Magazine, Politico, Reddit / r/all, Reuters, The Hill, The Huffington Post, The New York Times, The Washington Post, Time, USA Today, Vice News'

def top_articles(event, context):
    """
    Returns 20 of the top articles over the last 24 hours
    """
    params = {
        'language': 'en',
        'sortBy': 'popularity',
        'from': datetime.now() - timedelta(hours=24),
        'pageSize': '100',
        'sources': sources
    }
    news_articles = requests.get(
        'https://newsapi.org/v2/everything',
        params=params,
        headers={'Authorization': os.getenv('NEWS_API_KEY', '')}
    )
    selected_articles = select_parse_random(json.loads(news_articles.text))
    analyzed_articles = analyze_descriptions(selected_articles)
    response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': "*",
            'Access-Control-Allow-Credentials': True
        },
        'body': json.dumps(analyzed_articles)
    }
    return response

def query_article(event, context):
    """
    Returns 20 of the top articles over the last 24 hours for the given query
    """
    query = event['queryStringParameters']['query']
    params = {
        'q': query,
        'language': 'en',
        'sortBy': 'popularity',
        'from': datetime.now() - timedelta(hours=24),
        'pageSize': '100',
        'sources': sources
    }
    news_articles = requests.get(
        'https://newsapi.org/v2/everything',
        params=params,
        headers={'Authorization': os.getenv('NEWS_API_KEY', '')}
    )
    selected_articles = select_parse_random(json.loads(news_articles.text))
    analyzed_articles = analyze_descriptions(selected_articles)
    response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': "*",
            'Access-Control-Allow-Credentials': True
        },
        'body': json.dumps(analyzed_articles)
    }
    return response

def select_parse_random(news_articles):
    """
    Takes given news articles and returns a max of 20 random articles, leaving only important data
    @TODO: Figure out how to make this better. 20 random articles isn't the best representation of the days news.
    """
    indexes = []
    if len(news_articles['articles']) < 20:
        indexes = range(0, len(news_articles))
    else:
        indexes = random.sample(range(0, len(news_articles['articles'])), 20)
    random_popular_stories = []
    for index in indexes:
        random_popular_stories.append(news_articles['articles'][index])
    parsed_stories =  list(
        map(
            lambda x: {'title': x['title'], 'publication': x['source']
                       ['name'], 'url': x['url'], 'description': x['description']},
            random_popular_stories
        )
    )
    return parsed_stories

def analyze_descriptions(articles):
    """
    Adds political bias to each article
    """
    for article in articles:
        text_to_analyze = article['title']
        if article['description'] is not None:
            text_to_analyze = text_to_analyze + '. ' + article['description']
        params = {
            'data': text_to_analyze
        }
        political_analysis = requests.post(
            'https://apiv2.indico.io/political',
            data=json.dumps(params),
            headers={
                'X-ApiKey': os.getenv('INDICO_KEY', '')
            }
        )
        title_descrip_bias = json.loads(political_analysis.text)['results']
        if political_analysis.status_code == 200:
            highest_view = 0
            highest_bias = None
            for key in title_descrip_bias.keys():
                if title_descrip_bias[key] > highest_view:
                    highest_view = title_descrip_bias[key]
                    highest_bias = key
                elif title_descrip_bias[key] == highest_view:
                    highest_bias = 'Neutral'
            if highest_bias in ['Liberal', 'Green']:
                article['articleBias'] = 'Liberal'
            elif highest_bias is 'Neutral':
                article['articleBias'] = 'Neutral'
            else:
                article['articleBias'] = 'Conservative'
        else:
            article['articleBias'] = 'Unknown'
    return articles
