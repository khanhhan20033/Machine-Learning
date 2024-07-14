import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(2, 10, 20).reshape(-1,1)
#X = np.array([6.7, 4.6, 3.5, 5.5]).reshape(-1, 1)
print(X.shape)
noise = np.random.random(X.shape[0]).reshape(-1, 1)
y = (2 * X + 3 + 3 * noise).reshape(-1, 1)
print(y)
mean = np.mean(X)

X = (X - mean) / max(X)
epoch = 100
learning_rate = 0.01

X = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)
print(X)

w = np.random.random(2).reshape(-1,1)
lost = []
print(w)
for i in range(epoch):
    lst = []
    n=np.random.permutation(X.shape[0])
    X_shuffle=X[n]
    for j in n:
        x = np.array([X_shuffle[j, :]])
        print(x.T)
        w = w - learning_rate * (x.T.dot(x.dot(w) - y[j]))
        lst.append(0.5 * (x.dot(w) - y[j]) ** 2)
    lost.append(np.sum(np.array(lst)))
plt.title("Error")
plt.xlabel('iteration')
plt.ylabel('Lost')
plt.plot(lost)
plt.show()
