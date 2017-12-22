from __future__ import print_function
import tensorflow as tf
import numpy as np


x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights * x_data + biases

loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)

train = optimizer.minimize(loss)

session = tf.Session()

if int((tf.__version__).split(".")[1]) < 12 and int((tf.__version__).split(".")[0]) < 1:
    init = tf.initialize_all_variables()
else :
    init = tf.global_variables_initializer()
session.run(init)

for step in range(201):
    session.run(train)
    if step % 20 == 0:
        print(step, session.run(Weights), session.run(biases))