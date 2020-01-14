# 모듈 로딩
import os
import random
import re

import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from urllib import request

# csv 데이터 읽기
csv_url = 'https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/data/iris.csv'
csv_file = './iris.csv'

# 파일 없으면 온라인에서 다운로드.
if not os.path.isfile(csv_file):
    request.urlretrieve(csv_url, csv_file)

# 붓꽃 데이터 수집
csv = pd.read_csv(csv_file)

# 필요한 데이터(column) 추출
csv_data = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
csv_label = csv[['Name']]

# 학습 데이터와 테스트 데이터 분류
train_data, test_data, train_label, test_label = train_test_split(
    csv_data, csv_label)

# 데이터 학습 & 예측
clf = svm.SVC()
clf.fit(train_data, train_label)    # 학습
pre = clf.predict(test_data)        # 테스트

# 정확도 검사
as_score = metrics.accuracy_score(test_label, pre)
print('정답률 =', as_score)
