import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from get_dataset import get_dataset_file


def random_forest():
    print('========== RandomForestClassifier ==========')
    # 학습하기
    model = RandomForestClassifier()
    model.fit(x_train, y_train)

    # 평가하기
    y_pred = model.predict(x_test)
    print(classification_report(y_test, y_pred))
    print('정답률 =', accuracy_score(y_test, y_pred))


def svm_svc():
    print('========== SVM ==========')
    # 데이터 학습, 예측
    clf = svm.SVC()
    clf.fit(x_train, y_train)

    # 평가하기
    y_pred = clf.predict(x_test)
    print(classification_report(y_test, y_pred))
    print('정답률 =', accuracy_score(y_test, y_pred))


if __name__ == "__main__":
    DEBUG = True

    # 파일 있는지 확인
    url = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
    savepath = "wine_dataset/winequality-white.csv"
    get_dataset_file(url, savepath)

    # 데이터 읽기
    wine = pd.read_csv(savepath, sep=';', encoding='utf-8')
    if DEBUG:
        print(wine)

    # 데이터와 레이블 분리
    y = wine['quality']
    x = wine.drop('quality', axis=1)

    # 학습 데이터, 테스트 데이터 분리
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    if DEBUG:
        print('train data {} / test data {}\n'.format(
            x_train.shape[0], x_test.shape[0]))

    # 학습하기
    random_forest()
    print()
    svm_svc()
