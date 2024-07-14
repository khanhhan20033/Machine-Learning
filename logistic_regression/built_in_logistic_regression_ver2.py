import numpy as np
import matplotlib.pyplot as plt


def sigmoid(s):
    return 1 / (1 + np.exp(-s))


X = np.linspace(3, 10, 20).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]).reshape(-1, 1)
print(y.shape)
plt.plot(X[y == 1], y[y == 1], 'rs', markersize=8)
plt.plot(X[y == 0], y[y == 0], 'bo', markersize=8)
# plt.show()
epoch = 1000
X = np.concatenate((X, np.ones((X.shape[0], 1))), axis=1)
learning_rate = 0.01
w = np.random.random(2).reshape(-1, 1)
for i in range(epoch):
    w_old = w
    w = w + learning_rate * (X.T.dot(y - sigmoid(X.dot(w))))
    if np.linalg.norm(w - w_old) <= 10e-8:
        break
print(w)
xx = np.linspace(2, 11, 10000).reshape(-1, 1)
xx = np.c_[xx, np.ones((xx.shape[0], 1))]
yy = sigmoid(xx.dot(w))
plt.plot(xx[:, 0], yy, 'g-', lw=3)
threshold = -w[1] / w[0]
plt.plot(threshold, 0.5, 'y^', markersize=8)
plt.show()
x = 4
print("y_pred:")
print(sigmoid(w[0] * x + w[1]))
