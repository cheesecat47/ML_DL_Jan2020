from sklearn import svm, metrics
import glob
import os.path
import re
import json

# 텍스트 중 알파벳 출현 빈도 조사 함수


def check_freq(fname):
    name = os.path.basename(fname)
    print('name => {}'.format(name))

    # 파일 이름 앞에 알파벳 2게 시작 파일 체크
    lang = re.match(r'^[a-z]{2,}', name).group()  # 첫 번째 문자열 반환 / 언어 코드
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()

    text = text.lower()  # 소문자 변환
    # 숫자 세기 변수(cnt) 초기화하기
    cnt = [0 for n in range(26)]
    code_a = ord('a')
    code_z = ord('z')

    # 알파벳 출현 횟수 계산
    for ch in text:
        n = ord(ch)
        if code_a <= n <= code_z:
            cnt[n-code_a] += 1

    total = sum(cnt)
    freq = list(map(lambda n: n/total, cnt))  # 파일별 동일 조건 만들기
    return (freq, lang)


# 파일 로딩 기능
def load_files(path):
    freqs = []
    labels = []
    file_list = glob.glob(path) # 경로를 주면 파일 리스트 반환
    if DEBUG:
        print('file_list = {}'.format(file_list))

    for fname in file_list:
        if DEBUG:
            print('fname => {}'.format(fname))
        r = check_freq(fname)
        if DEBUG:
            print('r => {}'.format(r))
        freqs.append(r[0])
        labels.append(r[1])
    return {'freqs': freqs, 'labels': labels}


if __name__ == "__main__":
    DEBUG = True

    # 데이터 준비하기
    data = load_files('LANG/train/*.txt')
    test = load_files('LANG/test/*.txt')

    # JSON으로 결과 저장하기
    with open('LANG/freq.json', 'w', encoding='utf-8') as fp:
        json.dump([data, test], fp)

    # 학습 및 예측
    clf = svm.SVC()
    clf.fit(data['freqs'], data['labels'])
    predict = clf.predict(test['freqs'])

    # 결과 테스트
    as_score = metrics.accuracy_score(test['labels'], predict)
    cl_report = metrics.classification_report(test['labels'], predict)
    print('정답률 =', as_score)
    print('리포트 =\n', cl_report)
