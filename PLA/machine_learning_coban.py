import numpy as np
import matplotlib.pyplot as plt


def predict(w, X):
    return np.sign(X.dot(w))


def perceptron(X, y, w_init):
    w = w_init
    while True:
        pred = predict(w, X)
        # find indexes of misclassified points
        mis_idxs = np.where(np.equal(pred, y) == False)[0]
        # print(np.where(np.equal(pred, y) == False))
        # number of misclassified points
        num_mis = mis_idxs.shape[0]
        if num_mis == 0:  # no more misclassified points
            return w
        # randomly pick one misclassified point
        random_id = np.random.choice(mis_idxs, 1)[0]
        # update w
        w = w + y[random_id] * X[random_id]
    return w


means = [[-1, 0], [1, 0]]
cov = [[.3, .2], [.2, .3]]
N = 10
X0 = np.random.multivariate_normal(means[0], cov, N)
X1 = np.random.multivariate_normal(means[1], cov, N)
plt.plot(X0[:, 0], X0[:, 1], 'or', markersize=8)
plt.plot(X1[:, 0], X1[:, 1], '^b', markersize=8)

X = np.concatenate((X0, X1), axis=0)
y = np.concatenate((np.ones(N), -1 * np.ones(N)))
Xbar = np.concatenate((np.ones((2 * N, 1)), X), axis=1)
w_init = np.random.randn(Xbar.shape[1])
w = perceptron(Xbar, y, w_init)
print(Xbar.dot(w))
plt.plot(Xbar[:, 1], (-w[0] - w[1] * Xbar[:, 1]) / w[2], 'g-', lw=2)
plt.show()
