import cv2
import matplotlib.pyplot as plt

# 데이터 변수 선언
IMG_NAME = 'IMAGE/cat.jpg'
IMG_SAVE = 'IMAGE/cat_resize.jpg'
DEBUG = True

# 이미지 읽기
img = cv2.imread(IMG_NAME)

# 이미지 변경 및 저장
height, width, channel = img.shape
im2 = cv2.resize(img, (height * 2, width * 2))
ret = cv2.imwrite(IMG_SAVE, im2)

if DEBUG:
    print('ret = {}'.format(ret))
if ret:
    plt.imshow(cv2.cvtColor(im2, cv2.COLOR_BGR2RGB))
    plt.show()
else:
    print('-- SAVE FAIL')
