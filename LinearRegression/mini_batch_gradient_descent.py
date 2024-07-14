import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def mini_batch(X, w, m, y, learning_rate, epoch):
    ll = []
    for i in range(epoch):
        lst = []
        n = np.random.permutation(X.shape[0])
        X_shuffle = X[n]
        #print(X[n])
        #print(n)
        mm=0
        #print(X_shuffle)
        for j in range(0, len(X_shuffle), m):

            if j + m >= len(n):
                mm = len(X_shuffle)-j
            else:
                mm = m
            #print(n[j:j+mm])
            x = np.array(X_shuffle[j:j+mm, :])
            #print(x)
            w = w - learning_rate * (x.T.dot(x.dot(w) - y[j:j + mm]))
            ll.append(np.sum(0.5 * (x.dot(w) - y[j:j + mm]) ** 2))
        #ll.append(np.sum(np.array(lst)))
    return ll, w


df = pd.read_csv('data_lr.csv').values
# print(df)

X = df[:, :-1].reshape(-1, 1)
# = np.linspace(2, 10, 20).reshape(-1, 1)
# X = np.array([6.7, 4.6, 3.5, 5.5]).reshape(-1, 1)


noise = np.random.random(X.shape[0]).reshape(-1, 1)
# y = (2 * X + 3 + 3 * noise).reshape(-1, 1)
y = df[:, -1].reshape(-1,1)

# Determine the size of the training set
train_size = int(0.8 * (X.shape[0]))  # 80% for training, 20% for testing

# Shuffle the indices randomly
indices = np.random.permutation((X.shape[0]))

# Split the indices into training and testing sets
train_indices, test_indices = indices[:train_size], indices[train_size:]

# Split the data and labels using the selected indices
train_data, train_labels = X[train_indices], y[train_indices]
test_data, test_labels = X[test_indices], y[test_indices]
mean = np.mean(train_data)

train_data = (train_data - mean) / (max(train_data)-min(train_data))

ep = 1000
n = 0.01

train_data = np.concatenate((np.ones((train_data.shape[0], 1)), train_data), axis=1)

w = np.random.random(2).reshape(-1, 1)

m = 62

plt.title("Error")

plt.xlabel('iteration')
plt.ylabel('Lost')
lost, w = mini_batch(train_data, w, m, train_labels, n, ep)
test_data = np.concatenate((np.ones((test_data.shape[0], 1)), test_data), axis=1)

y_pred = np.dot(test_data, w)


data = np.concatenate((np.round(np.array([test_data[:, -1]]).T, 2), np.round(y_pred, 2)), axis=1)
plt.plot(lost)
#print(data)
plt.show()
file_name = 'result.csv'
np.savetxt(file_name, data, delimiter=',', fmt='%.2f')
