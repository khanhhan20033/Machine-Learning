import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

numOfPoint = 30
noise = np.random.normal(0, 1, numOfPoint)
#x = [6.7, 4.6, 3.5, 5.5]
#y = [9.1, 5.9, 4.6, 6.7]
x = np.linspace(30, 100, numOfPoint)
#print(x)
y = (15 * x + 8 + 20 * noise)
# print(y)
plt.scatter(x, y)
plt.title("Graph")
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()
# x1 = np.concatenate((np.ones((N, 1)), x), axis=1)
# print(x1.shape)
epoch = 12
learning_rate = 0.01
lost = []
w = np.array([2.1, 3.5])
# print(w)
# print(x1)
w1 = []
for i in range(epoch):
    lst = []
    for j in range(len(x)):
        e = np.c_[x[j], 1]
        # print(e)
        y_t = e.dot(w)
        # lst.append(0.5 * (y_t - y[j]) ** 2)
        w1.append(e.T.dot(y_t - y[j]))
    dw = np.mean(w1)
    w1 = []
    w = w - learning_rate * dw
    for k in range(len(x)):
        e = np.c_[x[k], 1]
        y_t = e.dot(w)
        lst.append(0.5 * (y_t - y[k]) ** 2)
    lost.append(np.mean(lst))
    print(lost[-1])
    lst = []
plt.title("Lost values")
plt.plot(lost)
plt.show()
