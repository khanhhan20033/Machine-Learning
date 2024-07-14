import numpy as np


def output(x, theta):
    return x.dot(theta)


def gradient(x, y, o):
    return 2 * x * (o - y)


def update_weight(theta, n, dt):
    return theta - n * dt


def loss(o, y):
    return (o - y) ** 2


data_x = [6.7, 8.6, 3.5, 5.5]
data_y = [9.1, 5.9, 4.6, 6.7]

n = 0.039
theta = np.array([2.1, 3.5])

for epoch in range(30):
    loss_avg = 0
    for i in range(len(data_x)):
        x = np.array([data_x[i], 1])
        y = data_y[i]

        # print(theta)
        o = output(x, theta)
        # print(i,y,o)

        l = loss(o, y)
        loss_avg = loss_avg + l

        dtheta = gradient(x, y, o)
        theta = update_weight(theta, n, dtheta)
    print(loss_avg / len(data_x))

for i in range(len(data_x)):
    x = np.array([data_x[i], 1], )
    y = data_y[i]
    o = output(x, theta)
    print(i, y, o)
