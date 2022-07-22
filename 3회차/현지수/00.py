import requests

def get_btc_krw():
    # URL
    order_currency = 'BTC'
    payment_currency = 'KRW'
    URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
    # 요청 보내서 파이썬 문법으로 바꿈
    response = requests.get(URL).json()
    # 바꿨을때 키값 넣으면 또 딕셔너리 나옴
    data = response["data"]
    # data 딕셔너리에서 전일종가 밸유값
    prev_closing_price = data["prev_closing_price"]
    # 그거 변수에 저장했으니 반환하는 함수 완성
    return prev_closing_price

# 이 조건문 뭐지...?
if __name__ == "__main__":
    print(get_btc_krw())