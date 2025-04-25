import numpy as np

arr = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

x = np.prod(arr)
print(x)  # Output: 24

# Calculate the product of all elements in arr2

y = np.prod([arr, arr2])
print(y)  # Output: 40320

# Calculate the product of all elements in arr2 along axis 0
z = np.prod([arr, arr2], axis=0)
print(z)  # Output: [ 5 12 21 32]
# Calculate the product of all elements in arr2 along axis 1
w = np.prod([arr, arr2], axis=1)
print(w)  # Output: [  24 1680]

# cumprod

arr3 = np.array([5,6,7,8])
x = np.cumprod(arr3)
print(x)  # Output: [  5 30 210 1680]