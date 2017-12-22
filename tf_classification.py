from __future__ import print_function
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('./data', one_hot=True)

def add_layer(inputs, in_size, out_size, activation_funcation=None,):
    Weights = tf.Variable(tf.random_nomal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1,)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_funcation is None :
        outputs = Wx_plus_b
    else :
        outputs = activation_funcation(Wx_plus_b)
    return outputs
def compute_accuracy(v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: v_xs})
    correct = tf.reduce_mean(tf.cast(correct_prec))


sess = tf.Session()