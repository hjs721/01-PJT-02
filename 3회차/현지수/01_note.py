# 3ebdebe4bdff8a78c64dc9f4bb38bf2e
# https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>

import requests

Base_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
     'api_key': '3ebdebe4bdff8a78c64dc9f4bb38bf2e',
     'language': 'ko-KR'
     }
response = requests.get(Base_URL+path, params=params).json()

print(type(response)) # <class 'dict'>
print(response.keys()) # dict_keys(['page', 'results', 'total_pages', 'total_results'])
print(type(response.get('results'))) # <class 'list'>
result = len(response.get('results'))
print(result) # 20