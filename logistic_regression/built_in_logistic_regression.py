import math

import numpy as np
import matplotlib.pyplot as plt


def sigmoid(s):
    return 1 / (1 + np.exp(-s))


X = np.linspace(3, 10, 20)
# X=np.array([X])
# print(X)
y = np.array([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1])
print(y.shape)
print(X[np.where(y == 1)])

epoch = 1000
learning_rate = 0.01
X = np.row_stack((X, np.ones(X.shape[0])))
w = np.random.random(2)
print(X)
print(w)
print(np.dot(w, X))
for i in range(epoch):
    w_old = w
    w = w + learning_rate * (y - sigmoid(np.dot(w, X))).dot(X.T)
    if np.linalg.norm(w - w_old) <= 10e-6:
        break

threshold = -w[0] / w[1]
# print(sigmoid(w .dot([10.5, 1])))
print(threshold)
# print(y_pred)
plt.plot(X[0, np.where(y == 1)][0], y[y == 1], 'rs', markersize=8)
xx=np.linspace(0, 10, 10000)

xx=(np.row_stack((xx, np.ones(xx.shape[0]))))
print(w.dot(xx))
plt.plot(X[0, np.where(y == 0)][0], y[y == 0], 'bo', markersize=8)
plt.plot(xx[0], sigmoid(w.dot(xx)), '-g', lw=2)
#plt.plot(threshold, 0.5, 'y^', markersize=8)

plt.ylim([-1,1.5])
plt.xlim(-2, 12)
plt.xlabel("Studying hour")
plt.ylabel("Probability of passing")
plt.show()
