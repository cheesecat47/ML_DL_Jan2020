import tensorflow as tf
import time

start = time.time()

# 노드 정의
a = tf.placeholder(tf.int32, [5])   # 플레이스홀더 노드 정의
two = tf.constant(2)    # 상수 노드 정의
x2_op = a * two  # 연산 노드 정의
print('[BEFORE]', a, two)

# 세션 생성
# s = tf.Session() # deprecated
with tf.compat.v1.Session() as s:
    # 연산 수행
    res1 = s.run(x2_op, feed_dict={a: [1, 2, 3, 4, 5]})
    res2 = s.run(x2_op, feed_dict={a: [5, 6, 7, 10, 100]})
    print('res1 = {}, res2 = {}'.format(res1, res2))

    # tf.summary.FileWriter('./logs', s.graph) # deprecated
    tf.compat.v1.summary.FileWriter('./logs', s.graph)

print("time :", time.time() - start)
