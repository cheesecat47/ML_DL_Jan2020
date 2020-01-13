from bs4 import BeautifulSoup


def sel(q):
    # CSS 선택자로 검색하는 방법
    return print(soup.select_one(q).string)


with open("books.html", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, "html.parser")

    sel("#nu")
    sel("li#nu")
    sel("ul > li#nu")
    sel("#bible #nu")
    sel("#bible > #nu")
    sel("ul#bible > li#nu")
    sel("li[id='nu']")
    sel("li:nth-of-type(4)")

    # 그 밖의 방법
    print(soup.select("li")[3].string)
    print(soup.find_all("li")[3].string)
