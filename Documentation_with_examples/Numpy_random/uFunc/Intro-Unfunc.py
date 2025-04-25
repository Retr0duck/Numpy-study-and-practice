import numpy as np

# Unfunc is a function that takes a numpy array as input and returns a new array with the same shape and data type as the input array, but with all elements set to 0.
x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[7, 8, 9], [10, 11, 12]])
z = np.onesadd(x, y)
print(z)