import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def gradient_sigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))


# read input from file .csv
data = np.genfromtxt('input.csv', delimiter=',', dtype=np.str_)
y = data[:, -1]
y = np.where(y == 'Iris-setosa', 1, 0)
data = np.genfromtxt('input.csv', delimiter=',')
X = data[:, :-1]

# split data into training and testing set
train_size = int(0.8 * X.shape[0])
indices = np.random.permutation(X.shape[0])
X_train, y_train = X[indices[:train_size]], y[indices[:train_size]]
X_test, y_test = X[indices[train_size:]], np.where(y[indices[train_size:]] == 0, 'Iris-virginica',
                                                   'Iris-setosa').reshape(-1, 1)

# Xuat ra file test.csv de so sanh voi ket qua du doan trong file predict.csv
test_set = np.hstack((X_test, y_test))
np.savetxt("Test.csv", test_set, fmt='%s')

# Data normalization
X_train = (X_train - np.mean(X_train)) / (np.max(X_train) - np.min(X_train))
X_train = np.hstack((X_train, np.ones((X_train.shape[0], 1))))

epoch = 100
learning_rate = 0.01
# weight initialization
w = np.random.random(5)

# Training
for i in range(epoch):
    idx = np.random.permutation(X_train.shape[0])
    w_new = w + learning_rate * (y_train[idx] - sigmoid(X_train[idx].dot(w))).dot(X_train[idx])
    if np.linalg.norm(w_new - w) <= 10e-8:
        break
    w = w_new
# normalize X_test
X_test1 = (X_test - np.mean(X_test)) / (np.max(X_test) - np.min(X_test))
X_test1 = np.concatenate((X_test1, np.ones((X_test1.shape[0], 1))), axis=1)

# predict
y_pred = sigmoid(X_test1.dot(w))
y_pred = np.where(y_pred >= 0.5, 'Iris-setosa', 'Iris-virginica')

# print(y_pred)

result = np.concatenate((X_test, y_pred.reshape(-1, 1)), axis=1)

# Xuat ket qua du doan
np.savetxt('predict.csv', result, fmt='%s')
