import requests


def popular_count():
    Base_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '3ebdebe4bdff8a78c64dc9f4bb38bf2e',
        'language': 'ko-KR'
        }
    response = requests.get(Base_URL+path, params=params).json()
    # print(response.keys()) # dict_keys(['page', 'results', 'total_pages', 'total_results'])
    return len(response.get('results')) 


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
