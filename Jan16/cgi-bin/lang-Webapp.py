#! ~/opt/anaconda3/envs/venv_mldl/bin/python
import cgi
import os.path
import joblib
import codecs
import sys

# python3 -m http.server --bind localhost --cgi 8080
# http, py 파일이 존재하는 폴더 바로 위에서 실행해야됨.

# web 인코딩 설정
# 표준 출력 인코딩 설정
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

# 검출기 로딩
pklfile = os.path.dirname(__file__) + '/freq.pkl'
clf = joblib.load(pklfile)      # 검사, 검출기 읽어오기

# 텍스트 입력 양식 출력하기


def show_form(text, msg=""):
    print("Content-Type: text/html; charset=utf-8")
    print("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8"> 
        <title>언어판별</title></head>
        <body><form>
        <textarea name="text" rows="8" cols="40"> {0} </textarea> 
        <p><input type="submit" value="판정"></p>
        <p> {1} </p>
        </form></body></html>
    """.format(cgi.html.escape(text), msg))

# 판정하기


def detect_lang(text):
    # 알파벳 출력 빈도 구하기
    text = text.lower()
    code_a, code_z = (ord('a'), ord('z'))
    cnt = [0 for i in range(26)]
    for ch in text:
        n = ord(ch)-code_a
        if 0 <= n < 26:
            cnt[n] += 1
    total = sum(cnt)
    if total == 0:
        return "입력이 없습니다."
    freq = list(map(lambda n: n/total, cnt))
    res = clf.predict([freq])

    # 언어 코드를 한국어로 변환하기
    lang_dic = {'en': '영어', 'fr': '프랑스어', 'id': '인도네시아어', 'tl': '타갈로그어'}
    return lang_dic[res[0]]

# Web 입력 양식 값 읽어들이기
form = cgi.FieldStorage()       # 입력폼 객체 가져오기
text = form.getvalue('text', default='')    # 폼 안의 텍스트 필드 값 읽어오기
print('text => {}'.format(text))
msg=""
if text != "":
    lang = detect_lang(text)
    msg = '판정 결과: '+lang
    print('msg = {}'.format(msg))

show_form(text, msg)

