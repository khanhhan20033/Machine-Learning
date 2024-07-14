# This is a sample Python script.
import numpy as np


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class KNN:
    def __init__(self):
        pass

    def distance_from_A_to_B(self, A, B):
        C = A - B
        return np.sum(np.square(C))

    def distance_from_A_to_vectorB(self, A, B):
        x = np.zeros_like((1, B.shape[0]))
        for i in range(B.shape[0]):
            x[0][i] = self.distance_from_A_to_B(A, B[i])
        return x

    def distance_from_A_to_vectorB_fast(self, A, B):
        A_1 = np.sum(np.square(A))
        # print(A_1)
        B_1 = np.sum(np.square(B), axis=1)
        # print(B_1)
        return A_1 + B_1 - 2 * np.dot(B, A)

    def distance_from_vectorA_to_vectorB(self, A, B):
        M = int(A.shape[0])
        N = int(B.shape[0])
        res = np.zeros((M, N))
        for i in range(M):
            # for j in range(M):
            # res[i][j] = self.distance_from_A_to_B(A[j], B[i])
            # print(B[i])
            # print(A)
            res[i] = self.distance_from_A_to_vectorB_fast(A[i], B)
        # print(res[i])
        return res

    def distance_from_vectorA_to_vectorB_fast(self, A, B):
        A_1 = np.sum(np.square(A), axis=1).reshape(-1, 1)
        # print(A_1)
        B_1 = np.sum(np.square(B), axis=1).reshape(1, -1)
        # print(B_1)
        return A_1 + B_1 - 2 * np.dot(A, B.T)


A = np.arange(30).reshape(6, 5)
B = np.arange(20).reshape(4, 5)
Knn = KNN()
print(Knn.distance_from_vectorA_to_vectorB(A, B))
