import tensorflow as tf
import time

start = time.time()

# 노드 정의
node1 = tf.constant(1234, name='a')  # 상수 노드 정의
node2 = tf.constant(1000, name='b')
add_op_node = node1 + node2  # 연산 노드 정의
print('[BEFORE]', node1, node2)

# 세션 생성
# s = tf.Session() # deprecated
s = tf.compat.v1.Session()

# 연산 수행
result = s.run(node1)
print('[AFTER] - RUN (node1) => ', result)
result = s.run([node1, node2])
print('[AFTER] - RUN [node1, node2] => ', result)
result = s.run(add_op_node)
print('[AFTER] - RUN add_op_node => ', result)

# 세션 종료
s.close()
print("time :", time.time() - start)
