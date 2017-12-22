import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

path = 'LogiReg_data.txt'
pdData = pd.read_csv(path, header=None, names=['Exam 1', 'Exam 2', 'Admitted'])
print(pdData.head())

positive = pdData[pdData['Admitted'] == 1]
negative = pdData[pdData['Admitted'] == 0]

#看看数据的情况
fig, ax = plt.subplots(figsize=(10, 5))
ax.scatter(positive['Exam 1'], positive['Exam 2'], s=30, c='b', marker='o', label='Admitted')
ax.scatter(negative['Exam 1'], negative['Exam 2'], s=30, c='r', marker='x', label='Not Admitted')
ax.legend()
ax.set_xlabel('Exam 1 Score')
ax.set_ylabel('Exam 2 Score')
#plt.show()

#1.sigmoid
#2.model
#3.cost
#4.gradient
#5.descent
#6.accuracy

#1.sigmoid
def sigmoid(z):
    return 1 / (1+np.exp(-z))

nums = np.arange(-10, 10, step=1)
fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(nums, sigmoid(nums), 'r')
#plt.show()

#2.model
def model(X, theta):
    return sigmoid(np.dot(X, theta.T))

#数据预处理
pdData.insert(0, 'Ones', 1)

orig_data = pdData.as_matrix()
cols = orig_data.shape[1]
X = orig_data[:, 0:cols -1 ]
y = orig_data[:, cols-1 : cols]

theta = np.zeros([1, 3])
print(X)
print(y)
print(theta)

#3.cost
def cost(X, y, theta):
    left = np.multiply(-y, np.log(model(X, theta)))
    right = np.multiply(1 - y, np.log(1 - model(X, theta)))
    return np.sum(left - right) / (len(X))

cost(X, y, theta)

#4.Gradient descent
def gradient(X, y, theta):
    grad = np.zeros(theta.shape)
    error = (model(X, theta) - y).ravel()
    for j in range(len(theta.ravel())):
        term = np.multiply(error, X[:, j])
        grad[0, j] = np.sum(term) / len(X)
    return grad


STOP_ITER = 0
STOP_COST = 0
STOP_GRAD = 0

def stopCriterion(type, value, threshold):
    if type == STOP_ITER:
        return value > threshold
    elif type == STOP_COST:
        return abs(value[-1] - value[-2]) < threshold
    elif type == STOP_GRAD:
        return np.linalg.norm(value) < threshold

import numpy.random

def shuffleData(data):
    np.random.shuffle(data)
    cols = data.shape[1]
    X = data[:, 0:cols - 1]
    y = data[:, cols - 1: ]
    return X, y

import time

def descent(data, theta, batchSize, stopType, thresh, alpha):
    init_time = time.time()
    i = 0  #迭代次数
    k = 0
    X, y = shuffleData(data)
    grad = np.zeros(theta.shape)
    costs = [cost(X, y, theta)]

    while True:
        grad = gradient(X[k:k+batchSize], y[k:k+batchSize], theta)
        k += batchSize
        if k >= n:
            k = 0


