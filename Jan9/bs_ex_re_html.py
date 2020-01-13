# HTML 파일 분석 및 출력 01 ------------------------------------------------------
from bs4 import BeautifulSoup
# # 분석하고 싶은 HTML
# html = """
# <html>
#     <body>
#         <h1 id="title">스크레이핑이란?</h1>
#         <p id="body">웹 페이지를 분석하는 것</p> 
#         <p>원하는 부분을 추출하는 것</p>
#     </body> 
# </html> 
# """

# soup = BeautifulSoup(html, 'html.parser')
# # 원하는 부분 추출하기
# h1 = soup.html.body.h1
# p1 = soup.html.body.p
# p2 = p1.next_sibling.next_sibling
# # 태그 포함해서 출력됨.
# print(h1)
# print(p1)
# print(p2)


# # find() 메서드 - 원하는 부분 추출
# title = soup.find(id="title")
# body = soup.find(id="body")
# print(title)
# print(body)

# # 텍스트 부분 출력하기
# print("#title=" + title.string) 
# print("#body=" + body.string)


# html2 = """
# <html>
#     <body>
#         <ul>
#             <li><a href="http://www.naver.com">naver</a></li> 
#             <li><a href="http://www.daum.net">daum</a></li>
#         </ul>
#     </body>
# </html>
# """

# soup = BeautifulSoup(html2, 'html.parser')
# links = soup.find_all("a")
# # 링크 목록 출력
# for a in links:
#     href = a.attrs['href']
#     text = a.string
#     print(text, ">", href)

