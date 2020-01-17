import cv2

# 데이터 변수 선언
IMG_NAME = 'IMAGE/test.jpg'
IMG_SAVE = 'IMAGE/test_copy.jpg'
DEBUG = True

# 이미지 읽기
img = cv2.imread(IMG_NAME)
if DEBUG:
    print('type(img) = {}'.format(type(img)))
    print('img.shape = {}'.format(img.shape))
    # print('img ====== \n{}\n'.format(img))

# 이미지 저장
ret = cv2.imwrite(IMG_SAVE, img)
if DEBUG:
    print('ret = {}'.format(ret))

print('Image Save OK!') if ret else print('--FAIL')
