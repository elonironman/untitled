
import tensorflow as tf

m1 = tf.constant([[2, 2]])
m2 = tf.constant([[3],[3]])

dot_operation = tf.matmul(m1, m2)

# 方法1
# session = tf.Session()
# result = session.run(dot_operation)
#
# print(result)
# session.close()


# 方法2
with tf.Session() as session:
    result = session.run(dot_operation)
    print(result)


from sklearn.naive_bayes import  GaussianNB
clf = GaussianNB()
clf.fit(x,y)

print(clf.predict())






























