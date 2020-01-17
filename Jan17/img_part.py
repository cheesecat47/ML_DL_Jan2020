import cv2
import matplotlib.pyplot as plt
from save_name import save_name


# 데이터 변수 선언
IMG_NAME = 'IMAGE/iu2.jpg'
IMG_SAVE = save_name(IMG_NAME, 'part')
DEBUG = True

# 이미지 읽기
img = cv2.imread(IMG_NAME)

# 이미지 변경 및 저장
height, width, channel = img.shape
h2 = int(height/3)
w2 = int(width/3)
im2 = img[0:h2, w2:w2*2]
ret = cv2.imwrite(IMG_SAVE, im2)

if DEBUG:
    print('ret = {}'.format(ret))
if ret:
    plt.imshow(cv2.cvtColor(im2, cv2.COLOR_BGR2RGB))
    plt.show()
else:
    print('-- SAVE FAIL')
