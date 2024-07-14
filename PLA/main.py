import numpy as np
import matplotlib.pyplot as plt


def sgn(X):
    if X >= 0:
        return 1
    return -1


def check(X, y, w):
    count = []
    index = []
    for i in range(X.shape[0]):
        # print(i)
        # print(abs(X[i].dot(w)))
        if (sgn(y[i] * X[i].dot(w))) < 0:
            count.append(X[i])
            index.append(i)
    if len(count) != 0:
        return np.concatenate((np.array(count), np.array([index]).reshape(-1, 1)), axis=1)
    return np.array([])


def check_ver2(X, y, w):
    count = []
    index = []
    for i in range(X.shape[0]):
        # print(i)
        # print(abs(X[i].dot(w)))
        if (sgn(y[i] * X[i].dot(w))) < 0:
            count.append(X[i])
            index.append(i)
    if len(count) != 0:
        return np.concatenate((np.array(count), np.array([index]).reshape(-1, 1)), axis=1), len(count)
    return np.array([]), 0


'''
def apply_PLA1(fname):
    dataa = np.genfromtxt(fname, delimiter=',', skip_header=1)
    data = dataa[:-1, 1:]
    # print(data)

    X = data[:, :-1]
    y = data[:, -1]

    y = np.where(y == 0, -1, 1)

    w = np.random.random(X.shape[1])

    # print(y)
    it = 0
    while True:
        it += 1
        misclassified_check = check(X, y, w)
        if misclassified_check.shape[0] == 0:
            print(f"w:{w}")
            # print(f"iteration:{it}")
            break
        # print(misclassified_check)
        np.random.shuffle(misclassified_check)
        for i in range(misclassified_check.shape[0]):
            #print(y[int(misclassified_check[i, -1])])
            # print(y[int(misclassified_check[i, -1])] * misclassified_check[i, :-1])
            w = w + y[int(misclassified_check[i, -1])] * misclassified_check[i, :-1]
            #print(w)
    y = np.where(y == -1, 0, 1)

    return X, y, w
'''
'''
def apply_PLA(fname):
    dataa = np.genfromtxt(fname, delimiter=',', skip_header=1)
    data = dataa[:-1, 1:]
    # print(data)
    train_size = int(0.8 * data.shape[0])
    indices = np.random.permutation(data.shape[0])

    X = data[:, :-1]
    y = data[:, -1]
    X_train = X[indices[:train_size]]
    y_train = y[indices[:train_size]]
    X_test = X[indices[train_size:]]
    y_test = y[indices[train_size:]]
    y_train = np.where(y_train == 0, -1, 1)
    # print(y_train)
    w = np.random.random(X.shape[1])
    # print(y)
    # y = np.where(y == 0, -1, 1)

    # print(y)
    it = 0
    while True:
        it += 1
        misclassified_check = check(X_train, y_train, w)
        if misclassified_check.shape[0] == 0:
            # print(f"w:{w}")
            # print(f"iteration:{it}")
            break
        # print(misclassified_check)
        np.random.shuffle(misclassified_check)
        for i in range(misclassified_check.shape[0]):
            # print(y[int(misclassified_check[i, -1])])
            w = w + y_train[int(misclassified_check[i, -1])] * misclassified_check[i, :-1]

    data_test = np.concatenate((X_test, y_test.reshape(-1, 1)), axis=1)
    np.savetxt("test_data.csv", data_test, fmt="%.2f")
    y_pred = X_test.dot(w)
    label = np.array([sgn(i) for i in y_pred])
    label = np.where(label == -1, 0, 1)
    data_pred = np.concatenate((X_test, label.reshape(-1, 1)), axis=1)
    np.savetxt("pred_data.csv", data_pred, fmt="%.2f")
    return X, y, w, label, y_test
'''


def apply_PLA2(fname):
    dataa = np.genfromtxt(fname, delimiter=',', skip_header=1)
    data = dataa[:-1, 1:]
    # print(data)

    X = data[:, :-1]
    y = data[:, -1]

    y = np.where(y == 0, -1, 1)

    w = np.random.random(X.shape[1])

    # print(y)
    it = 0
    epoch = 300
    min = 0
    for i in range(epoch):
        it += 1
        misclassified_check, length = check_ver2(X, y, w)

        if (i != 0 and length < min) or i == 0:
            min = length
            # print(f"iteration:{it}")
            # break

        # print(misclassified_check)
        np.random.shuffle(misclassified_check)
        for j in range(misclassified_check.shape[0]):
            w = w + y[int(misclassified_check[j, -1])] * misclassified_check[j, :-1]
            # print(w)
    y = np.where(y == -1, 0, 1)

    return X, y, w


''''
def accuracy(label, y_test):
    count = 0
    for i in range(label.shape[0]):
        if label[i] == y_test[i]:
            count += 1
    return count / y_test.shape[0]
'''''

# accurac = []
# epoch = 100
# for i in range(epoch):
# X, y, w, label, y_test = apply_PLA("Single Layer Perceptron Dataset.csv")
# accurac.append(accuracy(label, y_test))
# plt.title("Train accuracy")
# plt.plot(accurac)
# plt.xlabel("iteration")
# plt.ylabel("accuracy")
#
for i in range(4):
    X, y, w = apply_PLA2("Single Layer Perceptron Dataset.csv")
    plt.plot(X[np.where(y == 1), 1], X[np.where(y == 1), 2], 'or', markersize=8, label="Class1")
    plt.plot(X[np.where(y == 0), 1], X[np.where(y == 0), 2], '^b', markersize=8, label="Class2")
    print((-w[0] - w[1] * X[:, 1]) / w[2])
    # print([sgn(i) for i in X.dot(w.reshape(-1, 1))])
    plt.plot(X[:, 1], (-w[0] - w[1] * X[:, 1]) / w[2], '-g', lw=2,
             label="Classifier")
    # plt.legend(loc="lower left")
    plt.show()
