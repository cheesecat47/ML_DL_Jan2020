from sklearn import svm
import joblib
import json

# 각 언어의 출현 빈도 데이터(JSON) 읽어들이기
with open('LANG/freq.json', 'r', encoding='utf-8') as fp:
    d = json.load(fp)
    data = d[0]     # 파일별 데이터만 추출

# 데이터 학습하기
clf = svm.SVC()
clf.fit(data['freqs'], data['labels'])

# 학습 데이터 저장하기
joblib.dump(clf, 'LANG/freq.pkl')
print('ok')
