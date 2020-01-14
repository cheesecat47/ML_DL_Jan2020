# 모듈 로딩 -------------------------------------
import pandas as pd
from sklearn import svm, metrics

# XOR 연산
xor_input = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

# 입력을학습전용데이터와테스트전용데이터로분류
xor_df = pd.DataFrame(xor_input)
xor_data = xor_df.ix[:, 0:1]  # 데이터
xor_label = xor_df.ix[:, 2]  # 레이블

# 데이터 학습과 예측
clf = svm.SVC()
clf.fit(xor_data, xor_label)  # 학습
pre = clf.predict(xor_data)  # 예측

# 정답 추출
ac_score = metrics.accuracy_score(xor_label, pre)
print("정답률 =", ac_score)
