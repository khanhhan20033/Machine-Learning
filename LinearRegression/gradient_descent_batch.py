import numpy as np
import matplotlib.pyplot as plt

#X = np.linspace(2, 10, 20)
X = np.array([6.7, 4.6, 3.5, 5.5])
print(X)
noise = np.random.random(X.shape[0])
y = (2 * X + 3 + 3 * noise).reshape(-1, 1)
print(y.shape)
# plt.figure(figsize=(10,10))

plt.plot(X, y, 'ro', markersize=8)
plt.xlabel("Area", )
plt.ylabel("Price")
epoch = 1000
learning_rate = 0.01

X = np.concatenate((np.ones((X.shape[0], 1)), np.array([X]).T), axis=1)
print(X)
w = np.random.random((X.shape[1], 1))
for i in range(epoch):
    w_old = w
    # print(X.dot(w) - y)
    w = w - learning_rate * (X.T.dot(X.dot(w) - y))
    if np.linalg.norm(w - w_old) <= 10e-8:
        break
y_pred = X.dot(w)
print(y_pred)
# plt.subplot(2, 2, 1)
plt.plot(X[:, -1], y_pred, 'b-')
plt.show()
