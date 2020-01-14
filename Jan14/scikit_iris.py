# 모듈 로딩
import os
import random
import re

from sklearn import svm, metrics
from urllib import request

# csv 데이터 읽기
csv = []
csv_url = 'https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/data/iris.csv'
csv_file = './iris.csv'

# 파일 없으면 온라인에서 다운로드.
if not os.path.isfile(csv_file):
    request.urlretrieve(csv_url, csv_file)

with open(csv_file, 'r', encoding='utf-8') as fp:
    for line in fp:
        line = line.strip()
        cols = line.split(',')

        def fn(n): return float(n) if re.match(r'^[0-9\.]+$', n) else n
        cols = list(map(fn, cols))
        csv.append(cols)

    # for item in csv:
    #     print(item)

del csv[0]

random.shuffle(csv)

total_len = len(csv)
train_len = int(total_len * 2 / 3)
train_data = []
train_label = []
test_data = []
test_label = []

for i in range(total_len):
    data = csv[i][:4]
    label = csv[i][4]

    if i < train_len:
        train_data.append(data)
        train_label.append(label)
    else:
        test_data.append(data)
        test_label.append(label)

clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

as_score = metrics.accuracy_score(test_label, pre)
print('정답률 =', as_score)
