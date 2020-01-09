# HTML 파일 다운 & 분석 & 추출 ------------------------------------------------
from bs4 import BeautifulSoup
import urllib.request as req

# urlopen()으로 데이터 수집
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
res = req.urlopen(url)

# BeautifulSoup으로 분석
soup = BeautifulSoup(res, "html.parser")

# 원하는 데이터 추출
title = soup.find("title").string
wf = soup.find("wf").string
print(title)
print(wf)
