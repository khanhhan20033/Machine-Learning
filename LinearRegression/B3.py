import numpy as np


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
        x = np.append(data_x[i], 1)
        y = data_y[i]

        o = output(x, theta)

        l = loss(o, y)

        dtheta = gradient(x, y, o)
        dtheta_avg = dtheta_avg + dtheta
    theta_new = update_weight(theta, n, dtheta_avg / len(data_x))
    loss_avg = 0
    for i in range(len(data_x)):
        x = np.append(data_x[i], 1)
        y = data_y[i]

        o = output(x, theta_new)

        l = loss(o, y)
        loss_avg = loss_avg + l
    return theta_new, loss_avg / len(data_x)


Setosa = 0
Versicolor = 1
Virginica = 2

data = [[5.1, 3.5, 1.4, 0.2, Setosa],
        [4.9, 3, 1.4, 0.2, Setosa],
        [4.7, 3.2, 1.3, 0.2, Setosa],
        [4.6, 3.1, 1.5, 0.2, Setosa],
        [5, 3.6, 1.4, 0.2, Setosa],
        [5.4, 3.9, 1.7, 0.4, Setosa],
        [4.6, 3.4, 1.4, 0.3, Setosa],
        [5, 3.4, 1.5, 0.2, Setosa],
        [4.4, 2.9, 1.4, 0.2, Setosa],
        [4.9, 3.1, 1.5, 0.1, Setosa],
        [5.4, 3.7, 1.5, 0.2, Setosa],
        [4.8, 3.4, 1.6, 0.2, Setosa],
        [4.8, 3, 1.4, 0.1, Setosa],
        [4.3, 3, 1.1, 0.1, Setosa],
        [5.8, 4, 1.2, 0.2, Setosa],
        [5.7, 4.4, 1.5, 0.4, Setosa],
        [5.4, 3.9, 1.3, 0.4, Setosa],
        [5.1, 3.5, 1.4, 0.3, Setosa],
        [5.7, 3.8, 1.7, 0.3, Setosa],
        [5.1, 3.8, 1.5, 0.3, Setosa],
        [5.4, 3.4, 1.7, 0.2, Setosa],
        [5.1, 3.7, 1.5, 0.4, Setosa],
        [4.6, 3.6, 1, 0.2, Setosa],
        [5.1, 3.3, 1.7, 0.5, Setosa],
        [4.8, 3.4, 1.9, 0.2, Setosa],
        [5, 3, 1.6, 0.2, Setosa],
        [5, 3.4, 1.6, 0.4, Setosa],
        [5.2, 3.5, 1.5, 0.2, Setosa],
        [5.2, 3.4, 1.4, 0.2, Setosa],
        [4.7, 3.2, 1.6, 0.2, Setosa],
        [4.8, 3.1, 1.6, 0.2, Setosa],
        [5.4, 3.4, 1.5, 0.4, Setosa],
        [5.2, 4.1, 1.5, 0.1, Setosa],
        [5.5, 4.2, 1.4, 0.2, Setosa],
        [4.9, 3.1, 1.5, 0.2, Setosa],
        [5, 3.2, 1.2, 0.2, Setosa],
        [5.5, 3.5, 1.3, 0.2, Setosa],
        [4.9, 3.6, 1.4, 0.1, Setosa],
        [4.4, 3, 1.3, 0.2, Setosa],
        [5.1, 3.4, 1.5, 0.2, Setosa],
        [5, 3.5, 1.3, 0.3, Setosa],
        [4.5, 2.3, 1.3, 0.3, Setosa],
        [4.4, 3.2, 1.3, 0.2, Setosa],
        [5, 3.5, 1.6, 0.6, Setosa],
        [5.1, 3.8, 1.9, 0.4, Setosa],
        [4.8, 3, 1.4, 0.3, Setosa],
        [5.1, 3.8, 1.6, 0.2, Setosa],
        [4.6, 3.2, 1.4, 0.2, Setosa],
        [5.3, 3.7, 1.5, 0.2, Setosa],
        [5, 3.3, 1.4, 0.2, Setosa],
        [7, 3.2, 4.7, 1.4, Versicolor],
        [6.4, 3.2, 4.5, 1.5, Versicolor],
        [6.9, 3.1, 4.9, 1.5, Versicolor],
        [5.5, 2.3, 4, 1.3, Versicolor],
        [6.5, 2.8, 4.6, 1.5, Versicolor],
        [5.7, 2.8, 4.5, 1.3, Versicolor],
        [6.3, 3.3, 4.7, 1.6, Versicolor],
        [4.9, 2.4, 3.3, 1, Versicolor],
        [6.6, 2.9, 4.6, 1.3, Versicolor],
        [5.2, 2.7, 3.9, 1.4, Versicolor],
        [5, 2, 3.5, 1, Versicolor],
        [5.9, 3, 4.2, 1.5, Versicolor],
        [6, 2.2, 4, 1, Versicolor],
        [6.1, 2.9, 4.7, 1.4, Versicolor],
        [5.6, 2.9, 3.6, 1.3, Versicolor],
        [6.7, 3.1, 4.4, 1.4, Versicolor],
        [5.6, 3, 4.5, 1.5, Versicolor],
        [5.8, 2.7, 4.1, 1, Versicolor],
        [6.2, 2.2, 4.5, 1.5, Versicolor],
        [5.6, 2.5, 3.9, 1.1, Versicolor],
        [5.9, 3.2, 4.8, 1.8, Versicolor],
        [6.1, 2.8, 4, 1.3, Versicolor],
        [6.3, 2.5, 4.9, 1.5, Versicolor],
        [6.1, 2.8, 4.7, 1.2, Versicolor],
        [6.4, 2.9, 4.3, 1.3, Versicolor],
        [6.6, 3, 4.4, 1.4, Versicolor],
        [6.8, 2.8, 4.8, 1.4, Versicolor],
        [6.7, 3, 5, 1.7, Versicolor],
        [6, 2.9, 4.5, 1.5, Versicolor],
        [5.7, 2.6, 3.5, 1, Versicolor],
        [5.5, 2.4, 3.8, 1.1, Versicolor],
        [5.5, 2.4, 3.7, 1, Versicolor],
        [5.8, 2.7, 3.9, 1.2, Versicolor],
        [6, 2.7, 5.1, 1.6, Versicolor],
        [5.4, 3, 4.5, 1.5, Versicolor],
        [6, 3.4, 4.5, 1.6, Versicolor],
        [6.7, 3.1, 4.7, 1.5, Versicolor],
        [6.3, 2.3, 4.4, 1.3, Versicolor],
        [5.6, 3, 4.1, 1.3, Versicolor],
        [5.5, 2.5, 4, 1.3, Versicolor],
        [5.5, 2.6, 4.4, 1.2, Versicolor],
        [6.1, 3, 4.6, 1.4, Versicolor],
        [5.8, 2.6, 4, 1.2, Versicolor],
        [5, 2.3, 3.3, 1, Versicolor],
        [5.6, 2.7, 4.2, 1.3, Versicolor],
        [5.7, 3, 4.2, 1.2, Versicolor],
        [5.7, 2.9, 4.2, 1.3, Versicolor],
        [6.2, 2.9, 4.3, 1.3, Versicolor],
        [5.1, 2.5, 3, 1.1, Versicolor],
        [5.7, 2.8, 4.1, 1.3, Versicolor],
        [6.3, 3.3, 6, 2.5, Virginica],
        [5.8, 2.7, 5.1, 1.9, Virginica],
        [7.1, 3, 5.9, 2.1, Virginica],
        [6.3, 2.9, 5.6, 1.8, Virginica],
        [6.5, 3, 5.8, 2.2, Virginica],
        [7.6, 3, 6.6, 2.1, Virginica],
        [4.9, 2.5, 4.5, 1.7, Virginica],
        [7.3, 2.9, 6.3, 1.8, Virginica],
        [6.7, 2.5, 5.8, 1.8, Virginica],
        [7.2, 3.6, 6.1, 2.5, Virginica],
        [6.5, 3.2, 5.1, 2, Virginica],
        [6.4, 2.7, 5.3, 1.9, Virginica],
        [6.8, 3, 5.5, 2.1, Virginica],
        [5.7, 2.5, 5, 2, Virginica],
        [5.8, 2.8, 5.1, 2.4, Virginica],
        [6.4, 3.2, 5.3, 2.3, Virginica],
        [6.5, 3, 5.5, 1.8, Virginica],
        [7.7, 3.8, 6.7, 2.2, Virginica],
        [7.7, 2.6, 6.9, 2.3, Virginica],
        [6, 2.2, 5, 1.5, Virginica],
        [6.9, 3.2, 5.7, 2.3, Virginica],
        [5.6, 2.8, 4.9, 2, Virginica],
        [7.7, 2.8, 6.7, 2, Virginica],
        [6.3, 2.7, 4.9, 1.8, Virginica],
        [6.7, 3.3, 5.7, 2.1, Virginica],
        [7.2, 3.2, 6, 1.8, Virginica],
        [6.2, 2.8, 4.8, 1.8, Virginica],
        [6.1, 3, 4.9, 1.8, Virginica],
        [6.4, 2.8, 5.6, 2.1, Virginica],
        [7.2, 3, 5.8, 1.6, Virginica],
        [7.4, 2.8, 6.1, 1.9, Virginica],
        [7.9, 3.8, 6.4, 2, Virginica],
        [6.4, 2.8, 5.6, 2.2, Virginica],
        [6.3, 2.8, 5.1, 1.5, Virginica],
        [6.1, 2.6, 5.6, 1.4, Virginica],
        [7.7, 3, 6.1, 2.3, Virginica],
        [6.3, 3.4, 5.6, 2.4, Virginica],
        [6.4, 3.1, 5.5, 1.8, Virginica],
        [6, 3, 4.8, 1.8, Virginica],
        [6.9, 3.1, 5.4, 2.1, Virginica],
        [6.7, 3.1, 5.6, 2.4, Virginica],
        [6.9, 3.1, 5.1, 2.3, Virginica],
        [5.8, 2.7, 5.1, 1.9, Virginica],
        [6.8, 3.2, 5.9, 2.3, Virginica],
        [6.7, 3.3, 5.7, 2.5, Virginica],
        [6.7, 3, 5.2, 2.3, Virginica],
        [6.3, 2.5, 5, 1.9, Virginica],
        [6.5, 3, 5.2, 2, Virginica],
        [6.2, 3.4, 5.4, 2.3, Virginica],
        [5.9, 3, 5.1, 1.8, Virginica]]

import random as rd


def sep_for_iris_data():
    data_train = []
    data_test = []

    for d in data:
        if rd.randint(0, 1) == 0:
            data_train.append(d)
        else:
            data_test.append(d)

    return np.array(data_train), np.array(data_test)


def train_for_iris_data(data_train):
    data_train_x = data_train[:, :-1]
    data_train_y = data_train[:, -1]
    n = 1
    theta = np.random.rand((len(data_train_x[0]) + 1))
    loss_old = 1000000

    for epoch in range(100):

        theta_new, loss_avg = update_test(data_train_x, data_train_y, theta, n)
        if loss_avg < loss_old:
            theta = theta_new
            n = n * 1.5
            loss_old = loss_avg
            # print(loss_avg)
        else:
            n = n / 1.5

    return theta


def test_for_iris_data(data_test):
    data_x = data_test[:, :-1]
    data_y = data_test[:, -1]
    for i in range(len(data_x)):
        print(data_x[i])
        x = np.concatenate(np.array(data_x[i]),1)
        y = data_y[i]
        o = output(x, theta)
        print(i, y, o)


data_train, data_test = sep_for_iris_data()
theta = train_for_iris_data(data_train)
test_for_iris_data(data_test)


def test():
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
