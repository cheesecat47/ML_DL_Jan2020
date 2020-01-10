import requests
import json


def k2c(k): return k - 273.15


apikey = ''
with open('apikey', 'r', encoding='utf-8') as k:
    apikey += k.readline().strip()

cities = ["Seoul,KR", "Tokyo,JP", "New York,US"]
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"
print('api=>', api)

# 각 도시의 정보 추출 --------------------------------------------------------------------------------------
for name in cities:
    # API URL 구성
    url = api.format(city=name, key=apikey)
    print('url=>', url)

    # API에 요청을 보내 데이터 추출하기
    r = requests.get(url)

    # 결과를 JSON 형식으로 변환
    data = json.loads(r.text)
    print('data=>', data)

    # 결과 출력
    print("+ 도시 =", data["name"])
    print("| 날씨 =", data["weather"][0]["description"])
    print("| 최저 기온 =", k2c(data["main"]["temp_min"]))
    print("| 최고 기온 =", k2c(data["main"]["temp_max"]))
    print("| 습도 =", data["main"]["humidity"])
    print("| 기압 =", data["main"]["pressure"])
    print("| 풍향 =", data["wind"]["deg"])
    print("| 풍속 =", data["wind"]["speed"])
    print("")
