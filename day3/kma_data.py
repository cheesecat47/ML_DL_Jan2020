# 기상청 데이터 다운로드 예제
import urllib.request
import urllib.parse

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {'stnId': '108'}
params = urllib.parse.urlencode(values)
"""
urlencode를 거쳐서 stdId=108 이라는 스트링 타입으로 변환.
만약 여러개면 stnId=103&name=seoul 이런 식으로 바뀜.
"""

url = API + '?' + params
print('url = ', url)

data = urllib.request.urlopen(url).read()
text = data.decode('utf-8')
print(text)
