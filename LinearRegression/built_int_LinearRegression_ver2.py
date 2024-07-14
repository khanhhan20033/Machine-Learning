import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data_lr.csv', delimiter=',').values
np.random.shuffle(df)
# print(df)
X = df[:, :-1]
# X_train = np.arange(15)
# y_train=2*X_train+4+5*np.random.random(X_train.shape[0])
# X = np.row_stack((X, np.ones(X.shape)))
y = df[:, -1]
# indices = np.random.permutation(X.shape[0])
train_size = int(0.8 * X.shape[0])

# X_train, y_train = X[indices[:train_size]], y[indices[:train_size]]
# X_test, y_test = X[indices[train_size:]], y[indices[train_size:]]
X_train, y_train = X[:train_size], y[:train_size]
X_test, y_test = X[train_size:], y[train_size:]
mean = np.mean(X_train)
X_train = (X_train - mean) / (max(X_train) - min(X_train))
X_train = np.column_stack((X_train, np.ones((X_train.shape[0], 1))))

# X_train = np.concatenate((X_train, np.ones((X_train.shape[0], 1))), axis=1)
epoch = 1000
# w = np.random.random(2)
w = [-0.34, 0.45]
learning_rate = 0.001
lost = []
it = 0
for i in range(epoch):
    it += 1
    w_old = w
    n = np.random.permutation(X_train.shape[0])
    lst = 0
    # print(n)
    # n = range(X_train.shape[0])
    # print(X_train[n])
    # print()
    # print(n)
    for j in n:
        # print(X_train[j])
        y_ = X_train[j].dot(w)
        # lst=0.5*(y_-y_train[j])*(y_-y_train[j])


        lst = np.sum((0.5 * (y_ - y_train[j]) ** 2))
        lost.append(lst)
        if i==0:
            print(lst)
        # print(X_train[j])
        # print(w)
        w = w - learning_rate * (X_train[j].T.dot(y_ - y_train[j]))
    #print(lst)
    # print()
    #lost.append(lst)
    # print(lst)
    if np.linalg.norm(w - w_old) <= 10e-7:
        break
print(f"iterations:{it}")
plt.plot(X_train[:, 0], y_train, 'or', markersize=8)
plt.plot(X_train[:, 0], X_train.dot(w), '-b', lw=2)
plt.show()
plt.plot(lost)
plt.show()

print(w)
X_test = (X_test - np.mean(X_test)) / (max(X_test) - min(X_test))
X_test = np.concatenate((X_test, np.ones((X_test.shape[0], 1))), axis=1)
# print(X_train.dot(w))
# for i in range((X_test.shape[0])):
# print(X_test[i])
# print(f"{y_test[i]} {X_test[i].dot(w)}")

"""
from numpy import genfromtxt
import matplotlib.pyplot as plt
import  numpy as np
# pick data
data = genfromtxt('data_lr.csv', delimiter=',',skip_header=1)
areas = data[:, 0]
prices = data[:, 1]
print(areas)
N = areas.size
plt.scatter(areas, prices)
plt.xlabel('Diện tích nhà ')
plt.ylabel('Giá nhà ')
#plt.xlim(3, 7)
#plt.ylim(4, 10)
plt.show()
# param

areas=(areas-np.mean(areas))/(max(areas)-min(areas))
print(areas)
max_epoch = 1000
lr = 0.01
w, b = -0.34, 0.45
losses = []
for _ in range(max_epoch):
    for i in range(N):
        # select sample
        x = areas[i]
        y = prices[i:i + 1]
        # predict y_hat
        y_hat = w * x + b
        # compute loss
        loss = (y_hat - y) * (y_hat - y)
        losses.append(loss)
        # gradient
        d_w = 2 * x * (y_hat - y)
        d_b = 2 * (y_hat - y)
        # update
        w = w - lr * d_w
        b = b - lr * d_b
print("loss:\n", losses[-1])
plt.plot(losses)  # test with losses[3:]
plt.xlabel('iteration')
plt.ylabel('losses')
plt.show()

x_data = range(-2, 2)
y_data = [x * w + b for x in x_data]
plt.plot(x_data, y_data)
plt.scatter(areas, prices)
plt.xlabel('Diện tích nhà')
plt.ylabel('Giá nhà ')

#plt.xlim(3, 7)
#plt.ylim(4, 10)
plt.show()

"""
