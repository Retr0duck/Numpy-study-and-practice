"""Shuflling arrays"""
# shuffle the array means to randomly permute a sequence or return a permuted range.
# It is important to note that the permutation is done in-place, meaning that the original array is modified.
# The function returns the shuffled array.
from numpy import random
import numpy as np
# The random.shuffle() function is used to shuffle the contents of an array in-place.

# Example 1: Shuffle a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
random.shuffle(arr1)
print("Shuffled 1D array:", arr1)

# Example 2: Shuffle a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
random.shuffle(arr2)
print("Shuffled 2D array:\n", arr2)

# Example 3: Shuffle a 3D array 
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
random.shuffle(arr3)
print("Shuffled 3D array:\n", arr3)

"""Generation of random permutations"""
# The random.permutation() function is used to generate a random permutation of a sequence or return a permuted range.
a = np.array([1, 2, 3, 4, 5])
# Example 1: Random permutation of a 1D array
perm1 = random.permutation(a)
print("Random permutation of 1D array:", perm1)
# Example 2: Random permutation of a 2D array
perm2 = random.permutation(arr2)
print("Random permutation of 2D array:\n", perm2)
# Example 3: Random permutation of a range
perm3 = random.permutation(10)
print("Random permutation of range 10:", perm3)