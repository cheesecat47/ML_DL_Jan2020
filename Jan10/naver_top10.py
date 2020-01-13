if __name__ == "__main__":
    import requests
    from bs4 import BeautifulSoup

    url = 'https://www.naver.com/'
    keyword = 'span.ah_k'

    source = requests.get(url).text
    # print('source -> ', source)

    soup = BeautifulSoup(source, 'html.parser')
    hotkeys = soup.select(keyword)
    # print('hotkeys -> ', hotkeys)

    index = 0
    for key in hotkeys:
        index += 1
        print(str(index) + ': ' + key.text)
        if index >= 10:
            break
