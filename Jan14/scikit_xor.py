# 모듈 로딩 -------------------------------------
from sklearn import svm     # support vector machine – Classification기법
# 데이터 변수 선언 --------------------------------
# XOR 계산 결과 데이터
xor_data = [  # P, Q, result
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

# (1) 학습 데이터 추출 : 학습용 데이터와 레이블 분리
data = []
label = []
for row in xor_data:
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p, q])
    label.append(r)

# (2) 데이터 학습
clf = svm.SVC()
clf.fit(data, label)

# (3) 데이터 예측
pre = clf.predict(data)
print(" 예측결과:", pre)

# 결과 확인
ok = 0
total = 0
for idx, answer in enumerate(label):
    p = pre[idx]
    if p == answer:
        ok += 1
        total += 1
print("정답률:", ok, "/", total, "=", ok/total)
