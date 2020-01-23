import matplotlib.pyplot as plt
from keras.datasets import cifar10
from PIL import Image

# 데이터 변수 선언
(x_train, y_train), (x_test, y_test) = cifar10.load_data()  # Keras Dataset에서 다운받기

labels=['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']

# 이미지 출력 -------------------------------------
for i in range(40):
    img=Image.fromarray(x_train[i])    
    plt.subplot(5, 8, i+1)    
    plt.title(labels[y_train[i][0]])    
    plt.tick_params(bottom='off')    
    plt.tick_params(left='off')    
    plt.imshow(img)
plt.show()
