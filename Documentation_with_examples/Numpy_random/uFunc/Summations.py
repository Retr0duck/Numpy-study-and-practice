import numpy as np

# Summations
"""
Whats the difference between np.sum and np.add.reduce?
np.sum is a function that computes the sum of array elements over a given axis, while np.add.reduce is a ufunc that performs a reduction operation (in this case, addition) on the elements of an array. np.sum is more general and can handle multiple axes, while np.add.reduce is specifically for reducing an array using addition.
np.sum is a higher-level function that can handle more complex cases, while np.add.reduce is a lower-level operation that is more efficient for simple cases.
"""
# Example 1: Using np.sum
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2])
print(f"Using np.sum: {newarr}")

# Summation over an axis

print(f"Using np.sum with axis=0: {np.sum([arr1, arr2], axis=0)}")
print(f"Using np.sum with axis=1: {np.sum([arr1, arr2], axis=1)}")

# Cummulative Sum

print(f"Using np.cumsum: {np.cumsum(arr1)}")
