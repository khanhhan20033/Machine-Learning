import numpy as np

data=np.genfromtxt('Countries-exercise.csv',delimiter=',',skip_header=True)[:,1:]
print(data)