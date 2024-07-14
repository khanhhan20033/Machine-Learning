import numpy as np

import pandas as pd


def output(x, theta):
    return x.dot(theta)


def gradient(x, y, o):
    return 2 * x * (o - y)


def update_weight(theta, n, dt):
    return theta - n * dt


def loss(o, y):
    return (o - y) ** 2


def update_test(data_x, data_y, theta, n):
    dtheta_avg = np.zeros_like(theta)
    for i in range(len(data_x)):
        x = np.array([data_x[i], 1])
        y = data_y[i]

        o = output(x, theta)

        l = loss(o, y)

        dtheta = gradient(x, y, o)
        dtheta_avg = dtheta_avg + dtheta
    theta_new = update_weight(theta, n, dtheta_avg / len(data_x))
    loss_avg = 0
    for i in range(len(data_x)):
        x = np.array([data_x[i], 1])
        y = data_y[i]

        o = output(x, theta_new)

        l = loss(o, y)
        loss_avg = loss_avg + l
    return theta_new, loss_avg / len(data_x)


data_x = [6.7, 4.6, 3.5, 5.5]
data_y = [9.1, 5.9, 4.6, 6.7]
n = 1
theta = np.array([2.1, 3.5])
loss_old = 1000000
for epoch in range(100):

    theta_new, loss_avg = update_test(data_x, data_y, theta, n)
    if loss_avg < loss_old:
        theta = theta_new
        n = n * 1.5
        loss_old = loss_avg
        print(loss_avg)
    else:
        n = n / 1.5

for i in range(len(data_x)):
    x = np.array([data_x[i], 1], )
    y = data_y[i]
    o = output(x, theta)
    print(i, y, o)
