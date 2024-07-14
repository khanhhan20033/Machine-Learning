import numpy as np
from matplotlib import pyplot as plt


def softmax(X, w):
    # X:shape(N,d)
    # w:shape(d,C)
    z = X.dot(w)  # (N,C)
    exp_z = np.exp(z) / np.sum(np.exp(z), axis=1, keepdims=True)
    return exp_z


def softmax_stable(X, w):
    Z = X.dot(w)
    exp_z = np.exp(Z - np.max(X, axis=1, keepdims=True))
    return exp_z / np.sum(exp_z, axis=1, keepdims=True)


def softmax_loss(X, w, y):
    A = softmax_stable(X, w)
    N = X.shape[0]
    return -(1 / N) * np.sum(np.log(A[range(X.shape[0]), y]))


def softmax_grad(X, w, y):
    # X:shape(N,d)
    # A:shape(d,C)
    A = softmax_stable(X, w)

    A[range(X.shape[0]), y] -= 1

    # print(N)
    return X.T.dot(A)


def softmax_fit(X, y, w, batch_size=10, lr=0.01, epochs=100):
    loss_hist = [softmax_loss(X, w, y)]
    for i in range(epochs):
        idx = np.random.permutation(X.shape[0])
        for j in range(0, len(idx), batch_size):
            # print(idx[j])
            X_batch = X[idx[j:min(j + batch_size, X.shape[0])]]
            y_batch = y[idx[j:min(j + batch_size, y.shape[0])]]
            w = w - lr * softmax_grad(X_batch, w, y_batch)
        loss_hist.append(softmax_loss(X, w, y))
    return w, loss_hist


C, N = 5, 500  # number of classes and number of points per class
means = [[2, 2], [8, 3], [3, 6], [14, 2], [12, 8]]
cov = [[1, 0], [0, 1]]
X0 = np.random.multivariate_normal(means[0], cov, N)
X1 = np.random.multivariate_normal(means[1], cov, N)
X2 = np.random.multivariate_normal(means[2], cov, N)
X3 = np.random.multivariate_normal(means[3], cov, N)
X4 = np.random.multivariate_normal(means[4], cov, N)
X = np.concatenate((X0, X1, X2, X3, X4), axis=0)  # each row is a datapoint
Xbar = np.concatenate((X, np.ones((X.shape[0], 1))), axis=1)  # bias trick
y = np.asarray([0] * N + [1] * N + [2] * N + [3] * N + [4] * N)  # label
W_init = np.random.randn(Xbar.shape[1], C)

W, loss_hist = softmax_fit(Xbar, y, W_init)
print(loss_hist[0])
print(loss_hist[-1])
# print(np.where((pred(W, Xbar) - y) == 0))
plt.plot(loss_hist)
plt.show()
