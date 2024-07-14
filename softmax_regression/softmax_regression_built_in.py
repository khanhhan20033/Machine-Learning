import numpy as np
import matplotlib.pyplot as plt


def softmax(Z):
    return np.exp(Z) / np.sum(Z, axis=1, keepdims=True)


def softmax_stable(Z):
    z_max = np.max(Z, axis=1, keepdims=True)
    ez = np.exp(Z - z_max)
    return ez / np.sum(ez, axis=1, keepdims=True)


def softmax_loss(X, w, y):
    a = softmax_stable(X.dot(w))
    a_z = a[range(X.shape[0]), y]
    return -np.mean(np.log(a_z))


def softmax_grad(X, w, y):
    a = softmax_stable(X.dot(w))
    a[range(X.shape[0]), y] -= 1
    return X.T.dot(a) / X.shape[0]


def softmax_fit(X, w, y, lr=0.01, batch_size=10, epoch=100, tol=1e-5):
    w_old = w.copy()
    loss = [softmax_loss(X, w, y)]
    '''
    for i in range(epoch):
        n = np.random.choice(X.shape[0], batch_size, replace=False)
        print(n)
        print(i)
        w = w - lr * softmax_grad(X[n], w, y[n])
        print(w)
        loss.append(softmax_loss(X, w, y))
        print(loss)
        if np.linalg.norm(w - w_old) / np.prod(w.shape) <= tol:
            return loss, w
        w_old = w.copy()
    return loss,w
    '''
    for _ in range(epoch):
        mix_ids=np.random.permutation(X.shape[0])
        #print(X)
        for i in range(0, X.shape[0], batch_size):
            print(i)
            w -= lr * softmax_grad(X[mix_ids[i:min(i + batch_size, X.shape[0])]], w, y[mix_ids[i:min(i + batch_size, X.shape[0])]])
            loss.append(softmax_loss(X, w, y))
            #print(np.prod(w.shape))
            if np.linalg.norm(w - w_old) / np.prod(w.shape) < tol:
                return loss, w
            w_old = w.copy()
    return loss, w


C, N = 5, 500  # number of classes and number of points per class
means = [[2, 2], [8, 3], [3, 6], [14, 2], [12, 8]]
cov = np.array([[1, 0], [0, 1]])
X0 = np.random.multivariate_normal(means[0], cov, N)
X1 = np.random.multivariate_normal(means[1], cov, N)
X2 = np.random.multivariate_normal(means[2], cov, N)
X3 = np.random.multivariate_normal(means[3], cov, N)
X4 = np.random.multivariate_normal(means[4], cov, N)
X = np.row_stack((X0, X1, X2, X3, X4))
X = np.c_[X, np.ones((X.shape[0], 1))]
w = np.random.randn(X.shape[1], C)
y = np.array([0] * N + [1] * N + [2] * N + [3] * N + [4] * N)
#print(softmax_fit(X, w, y)[0])
loss, w = softmax_fit(X, w, y)
print(loss[0])
print(loss[-1])
plt.title("Ham mat mat")
plt.xlabel("iteration")
plt.ylabel("Loss")
plt.plot(loss)
plt.show()
