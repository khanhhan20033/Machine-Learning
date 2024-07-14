import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial.distance as d


# print(X[original_label==0].T[0])
# print(X[original_label==0])


def plot_k_means(xx, ll, kk):
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w']
    for i in range(kk):
        plt.plot(xx[ll == i].T[0], xx[ll == i].T[1], 'o', mec=colors[i], mfc=colors[i], alpha=0.8)

    plt.show()


def assign_labels(xx, centroids):
    #print( np.argmin(d.cdist(xx, centroids), axis=1))
    return np.argmin(d.cdist(xx, centroids), axis=1)


def find_centroids(xxx, ll, w):
    xx = np.random.random((3, 2))
    for i in range(w):
        #print(np.mean(xxx[ll == i], axis=0))
        xx[i, :] = np.mean(xxx[ll == i], axis=0)

    return xx


def init_(xx, k1):
    # print(xx[np.random.choice(xx.shape[0], k1, replace=False)])
    return xx[np.random.choice(xx.shape[0], k1, replace=False)]


def has_converged(c1, c2):
    count = 0
    for i in c1:
        #print(i)
        for j in c2:
            #print(j)
            if set(i) == set(j):
                count += 1
    if count == len(c1):
        return True
    return False


def k_means(xx, k1):
    centroids = init_(xx, k1)
    #print(xx)
    while True:
        label = assign_labels(xx, centroids)

        new_centers = find_centroids(xx, label, k1)
        if has_converged(centroids, new_centers):
            return centroids, label
        centroids = new_centers


N = 500
k = 3
x1 = [0, 2]
x2 = [3, 4]
x3 = [6, 4]
cov = [[1, 0], [0, 1]]
X1 = np.random.multivariate_normal(x1, cov, N)
X2 = np.random.multivariate_normal(x2, cov, N)
X3 = np.random.multivariate_normal(x3, cov, N)
X = np.concatenate((X1, X2, X3), axis=0)
lb = [[i] for i in range(k)]

original_label = np.array(lb[0] * 500 + lb[1] * 500 + lb[2] * 500)
plot_k_means(X, original_label, k)
centers, labels = k_means(X, k)
plot_k_means(X, labels, k)
print("centers found:")
print(centers)
