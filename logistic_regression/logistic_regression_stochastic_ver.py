import numpy as np
import matplotlib.pyplot as plt


def sigmoid(s):
    return 1 / (1 + np.exp(-s))


X = np.linspace(3, 12, 20)
y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
plt.plot(X[y == 1], y[y == 1], 'rs', markersize=8)
plt.plot(X[y == 0], y[y == 0], 'bo', markersize=8)
# plt.show()
epoch = 1000
X = np.concatenate((np.ones((1, X.shape[0])), np.array([X])), axis=0)
learning_rate = 0.01
w = np.random.random((1, 2))
for i in range(epoch):
    w_old = w
    for j in range(X.shape[1]):
        w = w + learning_rate * (y[j] - sigmoid(w.dot(X[:, j]))) * (X[:, j])
    if np.linalg.norm(w_old - w) <= 10e-8:
        break
xx = np.linspace(1, 13, 100)
xx = np.concatenate((np.ones((1, xx.shape[0])), np.array([xx])), axis=0)

plt.plot(xx[1].reshape(-1, 1), sigmoid(w.dot(xx))[0].reshape(-1, 1), 'g-', lw=2)
threshold = -w[0][0] / w[0][1]
print(threshold)
plt.plot(threshold, 0.5, 'y^', markersize=8)
plt.show()
