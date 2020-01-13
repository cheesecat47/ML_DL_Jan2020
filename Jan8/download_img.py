import urllib.request


def ex1():
    url = "https://cheesecat47.github.io//Photography/Infrared%20City/img/2019-1-4-infrared-city-181101_1.jpg"
    savename = "day3/testimg.jpg"

    urllib.request.urlretrieve(url, savename)
    print("Saved!")


def ex2():
    url = "https://cheesecat47.github.io//Photography/Infrared%20City/img/2019-1-4-infrared-city-181101_1.jpg"
    savename = "day3/testimgbin.jpg"

    mem = urllib.request.urlopen(url).read()

    with open(savename, mode='wb') as fi:
        fi.write(mem)
        print("Saved!")


if __name__ == "__main__":
    # ex1()
    ex2()
