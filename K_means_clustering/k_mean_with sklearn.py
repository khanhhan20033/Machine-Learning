import numpy as np
from KMeans import KMeans

data = np.genfromtxt('input.csv', delimiter=',')[:, :-1]

c = KMeans(4)
c.fit(data)
c.show()
#c.display_k_means(data)
c.K_choose(data)
