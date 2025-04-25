import numpy as np 

# Unique values
a = np.array([1, 2, 3, 4, 5, 1, 2])
x = np.unique(a)
print("Unique values in array:", x)     # This prints uniques values

b = np.array([6,6,6,7,8,8,9,9,9,9,10,10])
y = np.union1d(a, b)
print("Union of two arrays:", y)     # This prints the union of two arrays

c = np.intersect1d(a, b, assume_unique=True)
print("Intersection of two arrays:", c)     # This prints the intersection of two arrays

newarr = np.setdiff1d(a, b, assume_unique=True)
print("Set difference of two arrays:", newarr)     # This prints the set difference of two arrays

newarr2 = np.setxor1d(a, b, assume_unique=True)
print("Set symmetric difference of two arrays:", newarr2)     # This prints the set symmetric difference of two arrays