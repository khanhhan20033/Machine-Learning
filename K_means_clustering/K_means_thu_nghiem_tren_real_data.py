import numpy as np

from KMeans import KMeans

'''''
def plot_k_means(data, label):
    plt.title("real data")
    plt.plot(data[label == 0, 0], data[label == 0, 1], "or", markersize=8, alpha=0.8)
    plt.plot(data[label == 1, 0], data[label == 1, 1], "^b", markersize=8, alpha=0.8)
    plt.plot(data[label == 2, 0], data[label == 2, 1], "sg", markersize=8, alpha=0.8)
    plt.xlabel("Longtitude")
    plt.ylabel("Latitude")
    plt.show()
'''''

data = np.genfromtxt('Countries-exercise.csv', skip_header=True, delimiter=',')[:, 1:]
c = KMeans(2)
c.fit(data)
c.display_k_means(data)
c.K_choose(data)
c.show()
# print(len(data))
# k = 3
# labels = np.asarray([0] * 80 + [1] * 80 + [2] * 81)

# centers = np.array([[22, 30], [10, 20], [15, 17]])
'''''
plot_k_means(data, labels)


# plot_k_means(data, label)


def find_centroids(data, k):
    #print(data[np.random.choice(data.shape[0], k, replace=True)])
    return data[np.random.choice(data.shape[0], k, replace=True)]


def find_label(data, centers):
    # for j in centers:
    labels = []
    for i in data:
        lst = []
        for j in centers:
            lst.append(np.linalg.norm(i - j))
        lst = np.array(lst)
        # print(lst)
        labels.append(np.argmin(lst))
    return np.array(labels)


def find_centers(data, labels):
    centers = []
    for i in range(3):
        Xk = np.mean(data[labels == i], axis=0)
        centers.append(Xk)
    #print(np.array(centers))
    return np.array(centers)


def convert_to_list(centers, j):
    lst = []
    for i in centers:
        lst.append(i[j])
    return lst


def has_converged(center, centroid):
    c1_0 = convert_to_list(center, 0)
    c2_0 = convert_to_list(centroid, 0)
    c1_1 = convert_to_list(center, 1)
    c2_1 = convert_to_list(centroid, 1)
    return set(c1_0) == set(c2_0) and set(c1_1) == set(c2_1)


def K_means_algorithm(data):
    centroid = find_centroids(data, 3)
    while True:

        labels = find_label(data, centroid)
        centers = find_centers(data, labels)

        if has_converged(centroid, centers):
            return centers, labels
        centroid = centers


centers, labels = K_means_algorithm(data)
plt.title("real data")
plt.plot(data[labels == 0, 0:1], data[labels == 0, 1:2], "or", markersize=8, alpha=0.8)
plt.plot(data[labels == 1, 0:1], data[labels == 1, 1:2], "^b", markersize=8, alpha=0.8)
plt.plot(data[labels == 2, 0:1], data[labels == 2, 1:2], "sg", markersize=8, alpha=0.8)
plt.xlabel("Longtitude")
plt.ylabel("Latitude")
plt.plot(centers[0][0], centers[0][1], "oy", markersize=8)
plt.plot(centers[1][0], centers[1][1], "^y", markersize=8)
plt.plot(centers[2][0], centers[2][1], "sy", markersize=8)
plt.show()
'''''
