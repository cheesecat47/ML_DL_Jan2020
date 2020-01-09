# HTML 파일 분석 및 출력 : 네이버 금융 ------------------------------------------------
from bs4 import BeautifulSoup
import urllib.request as req

# HTML 가져오기
url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
res = req.urlopen(url)

# HTML 분석하기
soup = BeautifulSoup(res, "html.parser")

# 원하는 데이터 추출
price = soup.select_one(
    "ul#exchangeList>li.on>a.head>div.head_info>span.value").string
print("usd/krw =", price)
