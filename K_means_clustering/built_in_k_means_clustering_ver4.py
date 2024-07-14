import numpy as np
import matplotlib.pyplot as plt

N = 400
k = 3
centers = [[-1, 7], [-3, 1], [-9, 4]]
cov1 = np.array([[1, 0], [0, 1]])
cov2 = np.array([[11, 10], [0, 1]])
cov3 = np.array([[1, 10], [0, 1]])
X1 = np.random.multivariate_normal(centers[0], cov1, N)
X2 = np.random.multivariate_normal(centers[1], cov2, N)
X3 = np.random.multivariate_normal(centers[2], cov3, N)
X = np.concatenate((X1, X2))
X = np.concatenate((X, X3))
labels = np.array([0] * N + [1] * N + [2] * N)


def draw_k_means(X, labels, k):
    colors = ['r', 'g', 'b']
    for i in range(k):
        plt.plot(X[labels == i][:, [0]], X[labels == i][:, [1]], 'o', color=colors[i], markersize=8, alpha=0.7)
    plt.show()


draw_k_means(X, labels, k)


def _init_centers(X, k):
    return X[np.random.choice(X.shape[0], k)]


def find_labels(X, centers, k):
    labels = []
    for i in range(X.shape[0]):
        tmp = []
        for j in centers:
            j = np.array(j)
            X[i] = np.array(X[i])
            c = np.linalg.norm(X[i] - j)
            tmp.append(c)
        # print(tmp)
        labels.append(np.argmin(np.array(tmp)))
    return np.array(labels)


def find_centroids(X, labels, k):
    centroids = np.zeros((k, X.shape[1]))
    # print(centroids)
    for i in range(k):
        Xk = X[labels == i]

        centroids[i] = np.mean(Xk, axis=0)
    # print(centroids)
    # print(centroids)
    return centroids


def comp(x1, x2):
    c1 = []
    for i in range(x1.shape[0]):
        c1.append(x1[i])
    count = 0
    c2 = []
    for i in range(x2.shape[0]):
        c2.append(x2[i])
    # print(x1)
    # print(x2)
    for i in c1:
        for j in c2:
            if i == j:
                count += 1
                c1.remove(i)
                c2.remove(j)
    return count == len(c1)


def has_converged(centers, new_centers):
    c1 = []
    dct = {}
    for i in range(centers.shape[0]):
        c1.append(centers[i])
    count = 0
    c2 = []
    # print(new_centers)
    for i in range(new_centers.shape[0]):
        c2.append(new_centers[i])
        dct[i] = False
    # print(c1)
    for i in c1:
        for j in range(len(c2)):
            if comp(i, c2[j]) and dct[j] is False:
                dct[j] = True
                count += 1
    return count == len(c1)


def k_means(X, k):
    centers = _init_centers(X, k)
    # print(centers)
    while True:

        labels = find_labels(X, centers, k)
        # print(labels)
        new_center = find_centroids(X, labels, k)
        # print(new_center)
        if has_converged(centers, new_center):
            return centers, labels

        centers = new_center


centers, labels = k_means(X, k)
print(labels)
draw_k_means(X, labels, k)
print("new centers found {}".format(centers))