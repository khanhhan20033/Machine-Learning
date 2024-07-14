import numpy as np

my_array = np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [45, 65, 4, 2, 1]])

# Accessing elements
print(my_array)

print(my_array[0, np.where(my_array == 2)])  # Output: 1
print(my_array[1])  # Output: 3
print([np.where(my_array == 2)])
print(np.where([[True, False, True], [False, False, False]],
               [[1, 2,1], [3, 4, 1]],
               [[1, 122,7], [7, 6,4]]))
print(np.where([[True, False,False], [False, True,True]]))
print(my_array[0,np.where([[True, False,False], [False, True,True]])])
