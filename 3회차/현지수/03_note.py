import requests
from pprint import pprint


def ranking():
    Base_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '3ebdebe4bdff8a78c64dc9f4bb38bf2e',
        'language': 'ko-KR'
        }
    response = requests.get(Base_URL+path, params=params).json() # response.get('results') => list
    r_list = sorted(response.get('results'), key = lambda m: m['vote_average'], reverse = True)
    # sort, sorted 정리 :: https://infinitt.tistory.com/122
    return r_list
print(ranking())