"""

주의!!!
2~3시간 이상 걸릴 수 있음!

"""
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPool2D
from keras.optimizers import RMSprop
from keras.datasets import mnist
import matplotlib.pyplot as plt

import logging
logging.basicConfig(filename='mnist_cnn.log',
                    level=logging.DEBUG,
                    format='[%(asctime)s] %(name)s %(levelname)s \n%(message)s'
                    )
logger = logging.getLogger(__name__)

# 데이터변수 선언
im_rows = 28    # 이미지 높이
im_cols = 28    # 이미지 너비
im_color = 1    # 이미지 색공간 / 그레이스케일
in_shape = (im_rows, im_cols, im_color)
out_size = 10

# mnist 데이터 준비
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# mnist 데이터 가공
# 로딩 데이터 -> 3차원 배열 변환
X_train = X_train.reshape(-1, im_rows, im_cols, im_color)
X_train = X_train.astype('float32') / 255
X_test = X_test.reshape(-1, im_rows, im_cols, im_color)
X_test = X_test.astype('float32') / 255

# 레이블 데이터를 One-hot 형식으로 변환
y_train = keras.utils.np_utils.to_categorical(y_train.astype('int32'), 10)
y_test = keras.utils.np_utils.to_categorical(y_test.astype('int32'), 10)

# (4) CNN모델의 구조 정의------------------------
model = Sequential()

# 합성곱 레이어 -> 특징 추출 후 특징맵 생성
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu',
                 input_shape=in_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))

