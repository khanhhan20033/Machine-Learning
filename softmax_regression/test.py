import numpy as np

a = range(12)
print(a)
y = np.asarray([0, 1, 2, 1])
print(y[4:8].dot(np.array(a)))
