import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.linspace(0, 10, 20).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
w = np.random.random(2)
x = np.concatenate((x, np.ones((x.shape[0], 1))), axis=1)
'''''
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

y = np.array([1, 0, 0, 1])
x = np.concatenate((x, np.ones((x.shape[0], 1))), axis=1)
w = np.array([0, 0, 0])
'''''
learning_rate = 0.1
lst = []
for _ in range(1000):
    #i = np.random.choice(x.shape[0], 1)
    #print(np.array(x[i]))
    # w_new = w + learning_rate * (y[i[0]] - sigmoid(np.array([x[i[0]]]).dot(w))).dot(np.array([x[i[0]]]))
    w_new = w + learning_rate * x.T.dot(y - sigmoid(np.dot(np.array(x), w)))

    w = w_new
    # if (np.linalg.norm(w - w_new) / w_new.shape[0] <= 10e-8):
    # break
    lst.append(np.sum(-y * np.log(sigmoid(np.array(x).dot(w))) + (y - 1) * np.log(1 - sigmoid(np.array(x).dot(w))))/x.shape[0])
# print(w)
# print(np.array(x[y == 1][:, 0]).reshape(-1, 1))
lst = np.array(lst)
'''''
plt.plot(np.array(x[y == 1][:, 0]).reshape(-1, 1), y[y == 1], 'sr', markersize=8)
plt.plot(np.array(x[y == 0][:, 0]).reshape(-1, 1), y[y == 0], 'bo', markersize=8)
xx = np.linspace(0, 10, 1000).reshape(-1, 1)
xx = np.concatenate((xx, np.ones((xx.size, 1))), axis=1)

plt.plot(np.array(xx[:, 0]).reshape(-1, 1), sigmoid(xx.dot(w.reshape(-1, 1))), '-g', lw=2)
threshold = -w[1] / w[0]
plt.plot(threshold, .5, 'y^', markersize=8)
plt.show()
'''
# print(x[y == 0, :-1])
''''
plt.plot(x[y == 1, [0]], x[y == 1, [1]], 'or', markersize=8)
plt.plot(x[y == 0, [0]], x[y == 0, [1]], 'bo', markersize=8)
xx = np.linspace(0, 1, 1000).reshape(-1, 1)
plt.plot(xx, (-w[2] - w[0] * xx) / w[1], '-g', lw=2)
plt.show()
'''''
plt.plot(lst)
plt.xlabel("iteration")
plt.ylabel("Lost")
plt.show()
