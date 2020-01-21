import tensorflow as tf
import time

tftf = tf.compat.v1
thres = 0.001
start = time.time()


def err_func(cur: list, prev: list) -> list:
    if len(cur) != len(prev):
        return None
    temp = []
    for i in range(len(cur)):
        if cur[i] != 0:
            temp.append(abs((cur[i] - prev[i]) / cur[i]))
        else:
            temp.append(0)
    return temp


# 노드 정의
# 선형회귀 모델(Wx + b)을 정의
W = tf.Variable(tftf.random_normal(shape=[1]))
b = tf.Variable(tftf.random_normal(shape=[1]))
x = tftf.placeholder(tf.float32)
y = tftf.placeholder(tf.float32)

# 선형회귀 모델 연산 정의
linear_model = W*x + b
loss = tf.reduce_mean(tf.square(linear_model - y))  # 손실 함수 정의, mean-square

tftf.summary.scalar('loss', loss)  # 텐서보드 위한 요약정보(scala) 정의

# 최적화 그라디언트 디센트 / 러닝 레이트 => 학습 속도 설정
optimizer = tftf.train.GradientDescentOptimizer(0.01)
train_step = optimizer.minimize(loss)

# 트레이닝을 위한 입력값과 출력
x_train = [1, 2, 3, 4]
y_train = [2, 4, 6, 8]

# 세션 실행, 파라미터(W,b) 추출한 임의의 값으로 초기화
with tftf.Session() as sess:
    sess.run(tftf.global_variables_initializer())  # random_normal() 임의의 값 할당.
    
    # 텐서 보드 전달 정보 설정
    merged = tftf.summary.merge_all()  # 전달 정보 모두 합치기
    # 텐서 보드 summary 정보를 저장할 폴더 경로 설정
    tensorboard_writer = tftf.summary.FileWriter('./logs', sess.graph)

    # 모델 학습 실행: 경사하강법을 1000번 수행
    # 상대 에러 확인해서 0.01% 이하면 반복 종료
    err_W, err_b, prev_W, prev_b = 0, 0, 0, 0
    for i in range(10000):
        sess.run(train_step, feed_dict={
                 x: x_train, y: y_train})  # 학습데이터 지정 및 학습
        run_W = sess.run(W)
        run_b = sess.run(b)
        if i % 1000 == 0:
            print(i, run_W, run_b)

        # 매 스텝마다 텐서보드 요약정보값을 계산해서 지정된 경로에 저장
        summary = sess.run(merged, feed_dict={x: x_train, y: y_train})
        tensorboard_writer.add_summary(summary, i)

        # 에러율 확인
        if i > 0:
            err_W, err_b = err_func([run_W, run_b], [prev_W, prev_b])
            if err_W < thres and err_b < thres:
                print('{}th / err_W {} / err_b {}'.format(i, err_W, err_b))
                break
        prev_W, prev_b = run_W, run_b

    # 테스트 진행
    x_test = [3.5, 5, 5.5, 6]
    # 예상되는 참값: [7, 10, 11, 12]
    print(sess.run(linear_model, feed_dict={x: x_test}))

print("time :", time.time() - start)
