"""
Used to test if things work
"""
import os
import json
import requests
from datetime import datetime, timedelta

sources = 'ABC News, Al Jazeera English, Associated Press, Axios, Breitbart News, CBS News, CNN, Fox News, Google News, MSNBC, NBC News, Newsweek, New York Magazine, Politico, Reddit / r/all, Reuters, The Hill, The Huffington Post, The New York Times, The Washington Post, Time, USA Today, Vice News'

params = {
  'language': 'en',
  'country': 'us',
  'category': 'general'
}

params = {
    'language': 'en',
    'sortBy': 'popularity',
    'from': datetime.now() - timedelta(hours=24),
    'pageSize': '100',
    'sources': sources
}

response = requests.get(
  'https://newsapi.org/v2/everything',
  params=params,
  headers={'Authorization': 'b98b07dd05c5484f8c17a3363b6846fa'}
)

print(response.text)
