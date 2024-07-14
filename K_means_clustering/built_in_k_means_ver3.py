import numpy as np
import matplotlib.pyplot as plt

N = 200
K = int(input("nhap so lop can phan:"))
XX = []
for i in range(K):
    centers = np.random.random(2)
    XX.append(np.random.normal(loc=centers, scale=4, size=(N, 2)))
# X2 = np.random.normal(loc=(7, 4), scale=(2, 4), size=(N, 2))
# X3 = np.random.normal(loc=(5, 6), scale=(1, 1), size=(N, 2))
X = XX[0]
for i in range(1, K):
    X = np.row_stack((X, XX[i]))
# print(X)
origianl_labels = np.array([])
for i in range(K):
    origianl_labels = np.concatenate((origianl_labels, np.array([i] * N)))
# origianl_labels = np.array(origianl_labels)
print(origianl_labels.shape)


# print(np.where(origianl_labels==0))
# print(X[np.where(origianl_labels==0),])
def plot_k_means(X, labels, K):
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w']
    for i in range(K):
        plt.plot(X[np.where(labels == i), 0], X[np.where(labels == i), 1], 'o', color=colors[i], markersize=8,
                 alpha=0.8)
    plt.show()


plot_k_means(X, origianl_labels, K)


def K_means_init(X, k):
    return X[np.random.choice(X.shape[0], k, replace=False)]


def find_labels(X, centers):
    results = []
    for i in range(X.shape[0]):
        temp = []
        for j in range(centers.shape[0]):
            temp.append(np.linalg.norm(X[i] - centers[j]))
        # temp = np.array(temp)
        results.append(np.argmin(temp))
    # print(np.array(results))
    return np.array(results)


def find_centers(X, labels, k):
    results = []
    # print(X)
    for i in range(k):
        # print(labels==i)
        xi = np.mean(X[labels == i], axis=0)
        results.append(xi)
    # print(results)
    return np.array(results)


def compare(cc, cc1):
    count = 0
    for i in cc:
        for j in cc1:
            if i == j:
                count += 1
    return count == cc.shape[0]


def stop(centers, new_centers):
    count = 0
    for i in range(centers.shape[0]):
        for j in range(new_centers.shape[0]):
            print(centers[i])
            if compare(centers[i], new_centers[j]):
                count += 1
    return count == centers.shape[0]


def apply_k_means(X, k):
    centers = K_means_init(X, k)
    while True:
        labels = find_labels(X, centers)
        new_centers = find_centers(X, labels, k)
        if stop(centers, new_centers):
            return new_centers, labels
        centers = new_centers


centers, labels = apply_k_means(X, K)
plot_k_means(X, labels, K)
