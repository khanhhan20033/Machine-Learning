import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import cdist


def convert_to_list(x1, x2, index):
    lst = []
    lst_1 = []
    for i in x1:
        lst.append(i[index])
    for i in x2:
        lst_1.append(i[index])
    return lst, lst_1


class KMeans:
    def __init__(self, n_cluster):
        self.k = n_cluster
        self.centers = None
        self.labels = None
        self.distortion = None

    def initialize_centers(self, X):
        # print(X[np.random.choice(X.shape[0], self.k, replace=False)])
        return X[np.random.choice(X.shape[0], self.k, replace=False)]

    def find_labels(self, X, centers):
        # print(np.argmin(cdist(X, centers), axis=1))
        return np.argmin(cdist(X, centers), axis=1)

    def find_centers(self, X, labels):
        lst = []
        for i in range(self.k):
            # print(X[np.where(labels == i)])
            Xk = np.mean(X[np.where(labels == i)], axis=0)
            # print(Xk)
            lst.append(Xk)
        # print(lst)
        return np.asarray(lst)

    def has_converged(self, centers, centroids):
        lst0, lst0_1 = convert_to_list(centers, centroids, 0)
        lst1, lst1_1 = convert_to_list(centers, centroids, 1)
        return lst0 == lst0_1 and lst1 == lst1_1

    def fit(self, X):
        centers = self.initialize_centers(X)
        while True:
            labels = self.find_labels(X, centers)
            centroids = self.find_centers(X, labels)
            if self.has_converged(centers, centroids):
                self.centers = np.round(centers, 1)
                self.labels = labels
                self.distortion = np.sum(np.min(cdist(X, self.centers, 'euclidean'), axis=1))
                break
            centers = centroids

    def display_k_means(self, X):
        plt.scatter(X[:, 0], X[:, 1], c=self.labels, s=25)
        plt.show()

    def K_choose(self, X):
        lst = []
        for k in range(1, 11):
            c = KMeans(k)
            c.fit(X)
            lst.append(c.distortion)
        plt.title("Elbow method")
        plt.ylabel("Inertia")
        plt.xlabel("number of clusters")
        plt.plot(np.arange(1, 11).reshape(-1, 1), np.array(lst).reshape(-1, 1))
        plt.show()

    def show(self):
        print("Centers:  {}".format(self.centers))

data = np.genfromtxt('Countries-exercise.csv', skip_header=True, delimiter=',')[:, 1:]
c = KMeans(4)
c.fit(data)
c.display_k_means(data)
c.K_choose(data)
c.show()
'''''
Để xác định K(số cụm), chúng ta sử dụng phương pháp Elbow.
Phương pháp khuỷu tay là một kỹ thuật mà chúng ta sử dụng 
để xác định số lượng centroid (k) sẽ sử dụng trong thuật toán phân cụm k-mean.   
Trong phương pháp này để xác định giá trị k, chúng ta liên tục lặp lại từ k=1 đến k=n 
(Ở đây n là siêu tham số mà chúng ta chọn theo yêu cầu của mình). Đối với mỗi giá trị của k,
 chúng ta tính giá trị tổng bình phương (WCSS) trong cụm.
WCSS - Nó được định nghĩa là tổng bình phương khoảng cách giữa trọng tâm và
từng điểm của mỗi cụm.
Bây giờ để xác định số cụm (k) tốt nhất, chúng ta vẽ biểu đồ k so với giá trị WCSS của chúng.
 Điều đáng ngạc nhiên là đồ thị trông giống như một khuỷu tay . 
 Ngoài ra, khi k=1 thì WCSS có giá trị cao nhất nhưng khi giá trị k tăng thì giá trị WCSS bắt đầu giảm. 
 Chúng ta chọn giá trị k đó từ nơi đồ thị bắt đầu trông giống như một đường thẳng.
'''''
