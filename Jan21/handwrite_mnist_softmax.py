import tensorflow as tf

# 데이터 준비
# MNIST 데이터를 다운로드
# deprecated
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('./mnist_data/', one_hot=True)
# mnist = tf.keras.datasets.mnist
# (X_train, y_train), (X_test, y_test) = mnist.load_data()

# 입력값 & 출력값을 받기 위한 플레이스 홀더 정의
x = tf.compat.v1.placeholder(tf.float32, shape=[None, 784])  # 28*28
y = tf.compat.v1.placeholder(tf.float32, shape=[None, 10])  # 0~9 정답

# 변수 설정 및 softmax regression 모델 정의
W = tf.Variable(tf.zeros(shape=[784, 10]))
b = tf.Variable(tf.zeros(shape=[10]))
logits = tf.matmul(x, W) + b  # 차원 축소 4 => 3
y_pred = tf.nn.softmax(logits)  # 출력 차원별 확률로 변환

# cross-entropy 손실 함수와 옵티마이저를 정의
# 출력 N차원으로 N차원 값 합 & 평균
# loss = tf.reduce_mean(-tf.reduce_sum(y*tf.math.log(y_pred),
#                                      reduction_indices=[1]))
loss = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits, labels=y))

train_step = tf.compat.v1.train.GradientDescentOptimizer(0.5).minimize(loss)

# 세션을 열고 변수들에 초기값을 할당
sess = tf.compat.v1.Session()
sess.run(tf.compat.v1.global_variables_initializer())

# 1000번 반복을 수행하면서 최적화를 수행
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)  # 지정된 크기만틈 데이터 가져오기
    sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})
    # sess.run(train_step, feed_dict={x: X_train, y: y_train})

# 학습이 끝나면 학습된 모델의 정확도 출력
correct_prediction = tf.equal(tf.argmax(y_pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print("정확도(Accuracy): %f" % sess.run(accuracy, feed_dict={
      x: mnist.test.images, y: mnist.test.labels}))  # 정확도 : 약 91%
sess.close()
