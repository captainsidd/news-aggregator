import os
from dotenv import load_dotenv, find_dotenv
import requests

load_dotenv(find_dotenv())
query = input('Input your query: ')

params = {
  'q': query,
  'language': 'en',
  'sortBy': 'relevancy',
  'pageSize': '25',
}

response = requests.get(
  'https://newsapi.org/v2/everything', 
  params=params, 
  headers={'Authorization': os.getenv('NEWS_API_KEY', '')}
)

print(response.text)
