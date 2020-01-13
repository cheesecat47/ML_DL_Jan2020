# 모듈 로딩 --------------------------------------------------
import csv
import codecs

# CSV 파일 생성 -------------------------------------------
# encoding = euc_kr, utf-8
with codecs.open("./test_02.csv", "w", "utf-8") as fp:
    writer = csv.writer(fp, delimiter=",", quotechar='"')
    writer.writerow(["ID", "이름", "가격"])
    writer.writerow(["1000", "SD 카드", 30000])
    writer.writerow(["1001", "키보드", 21000])
    writer.writerow(["1002", "마우스", 15000])
