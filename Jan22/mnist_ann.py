import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 데이터 준비
mnist = input_data.read_data_sets('../Jan21/mnist_data/', one_hot=True)

# 학습 설정값 및 변수 정의
learning_rate = 0.001
num_epochs = 30  # 학습 횟수
batch_size = 256    # 배치 개수 1회 학습 데이터 수
display_step = 5    # 손실함수 출력 주기
input_size = 784    # 입력 데이터 => 28*28 픽셀
hidden1_size = 256  # 은닉층 노드(퍼셉트론) 개수
hidden2_size = 256  # 은닉층 노드(퍼셉트론) 개수
output_size = 10    # 출력 데이터 => 0~9 10개 레이블

# 입력값과 출력값 입력용 플레이스홀더 정의
x = tf.compat.v1.placeholder(tf.float32, shape=[None, input_size])
y = tf.compat.v1.placeholder(tf.float32, shape=[None, output_size])


def build_ANN(x):
    # ANN 모델 정의

    # 은닉층1: ReLU Activation Function 적용
    W1 = tf.Variable(tf.random.normal(shape=[input_size, hidden1_size]))
    b1 = tf.Variable(tf.random.normal(shape=[hidden1_size]))
    H1_output = tf.nn.relu(tf.matmul(x, W1) + b1)

    # 은닉층2: ReLU Activation Function 적용
    W2 = tf.Variable(tf.random.normal(shape=[hidden1_size, hidden2_size]))
    b2 = tf.Variable(tf.random.normal(shape=[hidden2_size]))
    H2_output = tf.nn.relu(tf.matmul(H1_output, W2) + b2)

    # 출력층: 은닉층 1,2의 출력값 Wx + b 가중합 계산
    W_output = tf.Variable(tf.random.normal(shape=[hidden2_size, output_size]))
    b_output = tf.Variable(tf.random.normal(shape=[output_size]))
    logits = tf.matmul(H2_output, W_output) + b_output  # 가중합
    # y_pred = tf.nn.softmax(logits)  # 출력 차원별 확률로 변환

    return logits


# ANN 모델 선언
predicted_value = build_ANN(x)

# 손실 함수와 옵티마이저 정의
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(
    logits=predicted_value, labels=y))
train_step = tf.compat.v1.train.AdamOptimizer(
    learning_rate=learning_rate).minimize(loss)

# 세션 & 그래프 실행
with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())  # 변수 초기값 할당

    # 지정된 횟수만큼 학습 최적화 수행
    for epoch in range(num_epochs):
        average_loss = 0
        total_batch = int(mnist.train.num_examples/batch_size)

        # 최적화 진행
        for i in range(total_batch):
            batch_x, batch_y = mnist.train.next_batch(batch_size)

            # 옵티마이저를 실행해서 파라미터 업데이트
            _, current_loss = sess.run([train_step, loss],
                                       feed_dict={x: batch_x, y: batch_y})
            # 평균 손실 측정
            average_loss += current_loss / total_batch

        # epoch마다 학습 결과 출력
        if epoch % display_step == 0:
            print('반복(epoch): {}, 손실함수(loss): {}'.format((epoch+1), average_loss))

    # 테스트 데이터 이용해서 학습된 모델 정확도 출력
    correct_prediction = tf.equal(
        tf.argmax(predicted_value, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float'))
    print('정확도(Accuracy): {}'.format(accuracy.eval(
        feed_dict={x: mnist.test.images, y: mnist.test.labels})))
