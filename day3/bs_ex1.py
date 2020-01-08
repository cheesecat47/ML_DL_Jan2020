from bs4 import BeautifulSoup

with open('testr.html', encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

    sel = lambda q: print(soup.select_one(q).string)
    sel("html")
    sel("body")

    # print(soup.select('p'))