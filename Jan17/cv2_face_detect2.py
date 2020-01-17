import matplotlib.pyplot as plt
import cv2
from save_name import save_name

# 데이터 변수 선언
HAAR_CASCADE_frontface = "CV_HAAR/haarcascade_frontalface_alt.xml"
HAAR_CASCADE_eye = "CV_HAAR/haarcascade_eye.xml"
IMG_FILE = 'IMAGE/iu1.jpg'
IMG_SAVE = save_name(IMG_FILE, 'detect')
DEBUG = True

# 캐스케이드 파일 지정해서 검출기 생성
cascade_frontface = cv2.CascadeClassifier(HAAR_CASCADE_frontface)
cascade_eye = cv2.CascadeClassifier(HAAR_CASCADE_eye)
if DEBUG:
    print('cascade = {}'.format(cascade_frontface))
    print('cascade = {}'.format(cascade_eye))

# 이미지를 읽어들이고 그레이스케일로 변환
img = cv2.imread(IMG_FILE)
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_h, img_w, img_ch = img.shape

# 얼굴 인식하기
# minSize, maxSize 조절.
face_size = int(min(img_h, img_w)/15)
eye_size = int(face_size/5)
if DEBUG:
    print('face_size = {}'.format(face_size))
    print('eye_size = {}'.format(eye_size))
face_list = cascade_frontface.detectMultiScale(
    img_grey, minSize=(face_size, face_size))
eye_list = cascade_eye.detectMultiScale(
    img_grey, minSize=(eye_size, eye_size))

# 결과 확인하기
if len(face_list) == 0:
    print('실패')
else:
    # 인식한 부분 표시하기
    for (x, y, w, h) in face_list:
        print('얼굴의 좌표: ', x, y, w, h)
        line_colour = (50, 50, 255)
        cv2.rectangle(img, (x, y), (x+w, y+h), line_colour, thickness=5)

if len(face_list) == 0:
    print('실패')
else:
    for (x, y, w, h) in eye_list:
        print('눈의 좌표: ', x, y, w, h)
        line_colour = (50, 255, 50)
        cv2.rectangle(img, (x, y), (x+w, y+h), line_colour, thickness=5)

# 이미지 출력하기
cv2.imwrite(IMG_SAVE, img)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
