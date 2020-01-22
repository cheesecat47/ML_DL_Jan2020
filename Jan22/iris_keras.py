import keras
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

import logging
logging.basicConfig(filename='iris_keras.log',
                    level=logging.INFO,
                    format='[%(asctime)s] %(name)s %(levelname)s \n%(message)s'
                    )

# 데이터 준비
# 붓꽃 데이터 읽기
iris_data = pd.read_csv('../Jan21/iris.csv', encoding='utf-8')

# 붓꽃 데이터를 레이블과 입력데이터로 분리
y_labels = iris_data.iloc[:, -1]  # iris name 라벨
x_data = iris_data.iloc[:, :-1]  # iris별 4가지 구분 데이터

# 레이블 데이터를 one-hot 형식으로 변환
labels = {
    'setosa': [1, 0, 0],
    'versicolor': [0, 1, 0],
    'virginica': [0, 0, 1]
}

y_nums = np.array(list(map(lambda v: labels[v], y_labels)))
x_data = np.array(x_data)

# 학습 전용과 테스트 전용으로 분리하기
x_train, x_test, y_train, y_test = train_test_split(
    x_data, y_nums, train_size=0.8)

# 모델 구조 정의
Dense = keras.layers.Dense
model = keras.models.Sequential()
model.add(Dense(10, activation='relu', input_shape=(4,)))
model.add(Dense(3, activation='softmax'))

# 모델 구축
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

# 학습 실행하기
model.fit(x_train, y_train, batch_size=20, epochs=300)

# 모델 평가하기
score = model.evaluate(x_test, y_test, verbose=1)
print('정답률: ', score[1])
print('loss= ', score[0])
