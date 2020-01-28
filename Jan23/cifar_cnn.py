import logging
import matplotlib.pyplot as plt
import keras
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.callbacks import History

import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'


# setting
base_name = 'cifar_cnn'
epoch = 30
activation1 = 'relu'
activation2 = 'softmax'
optimizer = keras.optimizers.Adam(0.001)
optimizer_name = 'adam'
dropout = 0.2

logging.basicConfig(filename='logs/{}_epoch{}_func{}_opt{}.log'.format(
                                base_name, epoch, activation1, optimizer_name),
                    level=logging.DEBUG,
                    format='[%(asctime)s] %(name)s %(levelname)s \n%(message)s'
                    )
logger = logging.getLogger(__name__)

logger.info("-------------------- Learning Settings --------------------")
logger.info('epoch = {}'.format(epoch))
logger.info('activation_functions = {}, {}'.format(activation1, activation2))
logger.info('optimizer = {}'.format(optimizer_name))
logger.info('dropout = {}'.format(dropout))
logger.info("-------------------- Start training! --------------------")

# 데이터 변수 선언
num_classes = 10
im_rows = 32
im_cols = 32
in_shape = (im_rows, im_cols, 3)
im_size = im_rows * im_cols * 3

# (1) 데이터 읽어 들이기 -----------------------------------
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
logger.info('-------------------- cifar10.load_data() --------------------')

# (2) 데이터가공 ------------------------------------------
# 3차원 변환 및 정규화
X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255
logger.info('-------------------- Reshaping. --------------------')

# 레이블 데이터를 One-hot 형식으로 변환
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
logger.info('-------------------- One-hot Encoding. --------------------')

# CNN 모델 정의하기
model = Sequential()

# convolution layers
model.add(Conv2D(32, (3, 3), padding='same', input_shape=in_shape))
model.add(Activation(activation1))
model.add(Conv2D(32, (3, 3)))
model.add(Activation(activation1))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(dropout))

model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation(activation1))
model.add(Conv2D(64, (3, 3)))
model.add(Activation(activation1))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(dropout))

model.add(Flatten())    # 3차원 -> 1차원
model.add(Dense(512))   # Dense가 1차원밖에 못 받음
model.add(Activation(activation1))
model.add(Dropout(dropout))
model.add(Dense(num_classes))
model.add(Activation(activation2))
logger.info('-------------------- Define CNN model --------------------')

# 모델 생성
model.compile(
    loss='categorical_crossentropy',
    optimizer=optimizer,
    metrics=['accuracy']
)
logger.info('-------------------- model.compile() --------------------')

# 학습 실행하기
# 전체 데이터 반복 횟수 epochs => 50
# 전체 데이터 1회 반복 시 학습 데이터 크기 32
# validation_data => 각 epoch마다 검증 데이터 정확도 출력
# validation_split => 데이터셋 비율
logger.info("-------------------- Start model.fit() --------------------")

hist = model.fit(X_train, y_train,
                 batch_size=32,
                 epochs=epoch,
                 verbose=1,
                 validation_data=(X_test, y_test),
                 callbacks=[
                     keras.callbacks.History(),
                     keras.callbacks.EarlyStopping(monitor='val_acc')
                     ]
                 )

# 모델 평가하기
score = model.evaluate(X_test, y_test, verbose=1)
logger.info('Accuracy: {} / loss: {}'.format(score[1], score[0]))
print('정답률=', score[1], ' / loss=', score[0])

# 학습 상태를 그래프로 그리기
plt.plot(hist.history['acc'])
plt.plot(hist.history['val_acc'])
plt.title('Accuracy')
plt.legend(['train', 'test'], loc='upper left')
try:
    plt .show()
except Exception as e:
    logger.error(e)

try:
    plt.savefig('results/{}_epoch{}_func{}_opt{}_{}.{}'.format(
            base_name, epoch, activation1, optimizer_name, 'accuracy', 'png'), dpi=72)
    plt.savefig('results/{}_epoch{}_func{}_opt{}_{}.{}'.format(
            base_name, epoch, activation1, optimizer_name, 'accuracy', 'svg'), dpi=72)
except Exception as e:
    logger.error(e)

plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Loss')
plt.legend(['train', 'test'], loc='upper left')
try:
    plt .show()
except Exception as e:
    logger.error(e)

try:
    plt.savefig('results/{}_epoch{}_func{}_opt{}_{}.{}'.format(
            base_name, epoch, activation1, optimizer_name, 'loss', 'png'), dpi=72)
    plt.savefig('results/{}_epoch{}_func{}_opt{}_{}.{}'.format(
            base_name, epoch, activation1, optimizer_name, 'loss', 'svg'), dpi=72)
except Exception as e:
    logger.error(e)

try:
    model.save_weights('results/{}_epoch{}_func{}_opt{}.{}'.format(
            base_name, epoch, activation1, optimizer_name, 'h5'))
except Exception as e:
    logger.error(e)
