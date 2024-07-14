import numpy as np
import pandas as pd

n = 0
D = 0
C = 0
df = pd.read_csv('bfs_dfs.csv')
for i in range(len(df.keys())):
    if i == 0:
        n = int(df.keys()[i])
    elif i == 1:
        D = int(df.keys()[i])
    elif i == 2:
        C = int(df.keys()[i])
A = df.values


# kiem tra xem da ket thuc chua (tuc la diem tai toa do (i,j) co phai la ria cua ma tran A khong)
def isFinished(A, i, j):
    if i + 1 == A.shape[0] or i - 1 == -1 or j + 1 == A.shape[0] or j - 1 == -1:
        return True
    return False


path = []

visited = []  # danh sach chua tat ca cac diem da di qua

parent = np.zeros((n, n, 2), dtype=np.int32)
parent[D, C] = [D, C]


def trace_path(ii, j):
    while parent[ii, j][0] != ii or parent[ii, j][1] != j:
        path.append([ii, j])

        old_param = ii
        old_param1 = j
        ii = parent[old_param, old_param1][0]

        j = parent[old_param, old_param1][1]
    path.append([ii, j])
    print(path)


def BFS(A, D, C):
    lst = [[D, C]]  # khoi tao danh sach diem can di qua

    while len(lst) != 0:

        pivot = lst.pop(0)  # Lay diem co chi so =0 ra khoi danh sach diem can di qua
        visited.append(pivot)
        # da di qua diem nay
        index_ = pivot
        if (A[index_[0]][index_[1] + 1] == 1 and [index_[0], index_[1] + 1] not in visited and
                [index_[0], index_[1] + 1]
                not in lst):
            parent[index_[0]][index_[1] + 1] = [index_[0], index_[1]]
            # print([index_[0], index_[1] + 1])

            if isFinished(A, index_[0], index_[1] + 1):
                trace_path(index_[0], index_[1] + 1)

                break

            lst.append([index_[0], index_[1] + 1])

        if (A[index_[0] + 1][index_[1]] == 1 and [index_[0] + 1, index_[1]] not in visited and [index_[0] + 1,
                                                                                                index_[1]]
                not in lst):
            parent[index_[0] + 1][index_[1]] = [index_[0], index_[1]]
            # print([index_[0] + 1, index_[1]])
            # print(parent)
            if isFinished(A, index_[0] + 1, index_[1]):
                trace_path(index_[0] + 1, index_[1])

                break

            lst.append([index_[0] + 1, index_[1]])

        if (A[index_[0] - 1][index_[1]] == 1 and [index_[0] - 1, index_[1]] not in visited and [index_[0] - 1,
                                                                                                index_[1]]
                not in lst):
            parent[index_[0] - 1][index_[1]] = [index_[0], index_[1]]
            # print([index_[0] - 1, index_[1]])
            if isFinished(A, index_[0] - 1, index_[1]):
                trace_path(index_[0] - 1, index_[1])

                break

            lst.append([index_[0] - 1, index_[1]])

        if (A[index_[0]][index_[1] - 1] == 1 and [index_[0], index_[1] - 1] not in visited and [index_[0],
                                                                                                index_[1] - 1]
                not in lst):
            parent[index_[0]][index_[1] - 1] = [index_[0], index_[1]]
            #  print([index_[0], index_[1] - 1])
            if isFinished(A, index_[0], index_[1] - 1):
                trace_path(index_[0], index_[1] - 1)

                break

            lst.append([index_[0], index_[1] - 1])


BFS(A, D, C)
row1 = []
for i in path:
    row1.append(i[0])
row2 = []
for i in path:
    row2.append(i[1])

import csv

# Danh sách kết quả cần ghi vào file CSV
results = [
    [str(len(path)), ''],

]
for i in range(len(path)):
    results.append([row1[i],row2[i]])
# Ghi dữ liệu vào file CSV
with open('bfs_dfs_out.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    for row in results:
        writer.writerow(row)

print("Kết quả đã được ghi vào file results.csv")
