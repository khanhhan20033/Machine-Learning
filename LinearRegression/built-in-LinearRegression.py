import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

numOfPoint = 30
noise = np.random.normal(0, 1, numOfPoint).reshape(-1, 1)
x = np.linspace(30, 100, numOfPoint).reshape(-1, 1)
N = x.shape[0]
y = 15 * x + 8 + 20 * noise
plt.scatter(x, y)
plt.title("Graph")
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()
x1 = np.concatenate((x, np.ones((N, 1))), axis=1)
# print(x)

inverse = np.linalg.pinv(x1.T.dot(x1))
inv = np.dot(x1.T, y)
w = inverse.dot(inv)
plt.title("Graph after training")
plt.scatter(x, y)
plt.xlabel('Area')
plt.ylabel('Price')
plt.plot(x, np.dot(x1, w),'-r')
plt.show()
