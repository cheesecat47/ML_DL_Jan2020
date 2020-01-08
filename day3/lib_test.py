def readEx():
    try:
        with open('day3/testr.html', mode='r', encoding='utf-8') as fr:
            for li in fr:
                print(li.rstrip())
    except FileNotFoundError as e:
        print(e)


def writeEx():
    try:
        with open('day3/testw.txt', mode='w', encoding='utf-8') as fw:
            for i in range(1, 6):
                data = "{}번째 줄\n".format(i)
                fw.write(data)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    readEx()
    writeEx()
