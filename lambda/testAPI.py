"""
Used to test if things work
"""
import os
import json
import requests

params = {
  'language': 'en',
  'country': 'us',
  'category': 'general'
}

response = requests.get(
  'https://newsapi.org/v2/sources',
  params=params,
  headers={'Authorization': #REDACTED}
)

sources_obj = json.loads(response.text)
names = list(map(lambda x: x['name'], sources_obj['sources']))
print(','.join(names))
