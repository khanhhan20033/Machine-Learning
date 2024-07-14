import numpy as np
import matplotlib.pyplot as plt


def process(X, w, y, n):
    w_init = w
    dtheta = np.zeros_like(w)
    for i in range(X.shape[1]):
        xi = X[:, i].reshape(-1, 1)
        # print(xi)
        dtheta += (w.dot(xi) - y[:, i]).dot(xi.T)
    # print(X.shape[1])
    w_init = w_init - n * (dtheta / X.shape[1])
    lst = 0
    for i in range(X.shape[1]):
        xi = X[:, i].reshape(-1, 1)

        lst += np.sum(0.5 * (w.dot(xi) - y[:, i]) ** 2)
    return lst / X.shape[1], w_init


X = np.linspace(0, 20, 20)
X = np.array([X])
noise = 15 * np.random.randn(1, X.shape[1])
y = 15 * X + 3 + noise
w = np.random.random((1, 2))
# print(X)
X = np.concatenate((X, np.ones((1, X.shape[1]))))
# print(np.mean(X))
X = (X - np.mean(X)) / (np.max(X) - np.min(X))

# print(X)
epoch = 100
learning_rate = 0.1
old_lost = 100000
lost = []
for i in range(epoch):
    lst, w_init = process(X, w, y, learning_rate)
    lost.append(lst)
    if lst < old_lost:
        learning_rate *= 1.5
        w = w_init
        old_lost = lst

    else:
        learning_rate /= 1.5
plt.plot(lost)
plt.show()

#print(X[0].reshape(-1, 1))

plt.plot(np.array([X[0]]), y, 'or', markersize=8)
plt.plot(X[0].reshape(-1, 1), w.dot(X)[0].reshape(-1,1), 'g-', lw=2)
print(w)
plt.show()
