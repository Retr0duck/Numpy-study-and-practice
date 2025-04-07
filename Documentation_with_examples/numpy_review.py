import numpy as np

"""Create a NumPy ndarray Object"""
# arr = np.array([[1,2,3], [4,5,6]]) # 2D array
# arr = np.array([1,2,3]) # 1D array
# arr3D = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]]) # 3D array
# print(arr3D.ndim) # 3
# print(arr.ndim) # 2
# arr = np.array([1,2,3,4], ndmin=5) # 5D array

# arr = np.array([1,2,3,4,5])
# print(arr[0])
# print(arr[2],arr[3]) # 3 4

"""Access 2-D Arrays"""
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print(arr[0,1]) # 2
# print(arr[1,2])

"""Access 3-D Arrays"""
# arr = np.array([1,2,3,4,5,6,7,8,9,10])
# print(arr[1:7])
# print(arr.dtype) # <U6

# arr = np.array([1,2,3,4,5,6,7,8,9,10], dtype='S')
# print(arr.dtype) # |S2
# print(arr[1:7]) # [b'2' b'3' b'4' b'5' b'6' b'7']

# arr = np.array([1.1, 2.1, 3.1])
# newarr = arr.astype(int)
# print(newarr) # [1 2 3]



"""Copy : The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy."""
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 42                          # x is not affected by the change in arr
# print(arr) # [42  2  3  4  5]
# print(x) # [1 2 3 4 5]


""" View : The view() method creates a new array object that looks at the same data."""
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# arr[0] = 42
# print(arr) # [42  2  3  4  5]
# print(x) # [42  2  3  4  5]
# output is same for both x and arr

"""Check if Array Owns it's Data"""
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# y = arr.view()
# print(x.base) # None
# print(y.base) # [1 2 3 4 5]
# The copy returns None.
# The view returns original array.
# The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
# The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view



"""Shape of an Array""" # The shape of an array is the number of elements in each dimension.
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(arr.shape) # (2, 4) 2 rows and 4 columns
# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr.shape) # (1, 1, 1, 1, 4) 1 row and 4 columns

"""Reshaping arrays"""
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(4, 3)
# print(newarr)
# newarr = arr.reshape(2, 3, 2) #  2 matrices, each with 3 rows and 2 columns
# print(newarr)

"""Flattening the arrays"""
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# newarr = arr.reshape(-1)
# print(newarr) result is [1 2 3 4 5 6]

"""Iterating Arrays"""
#arr = np.array([1, 2, 3]) # 1D array
#for x in arr: # 1 2 3
#    print(x)

# arr = np.array([[1, 2, 3], [4, 5, 6]]) # 2D array
# for x in arr: # [1 2 3] [4 5 6]
#     for y in x: # 1 2 3 4 5 6
#         print(y)


"""Iterating Arrays with 3D"""
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) # 3D array
# for x in arr:
#     for y in x: # [1 2 3] [4 5 6], [7 8 9] [10 11 12]
#         for z in y: # 1 2 3 4 5 6 7 8 9 10 11 12
#             print(z)

"""iterate with nditer()"""
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # 2D array
# for x in np.nditer(arr):
#     print(x) # 1 2 3 4 5 6

"""iterate with op_dtypes"""
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # 2D array
# for x in np.nditer(arr, flags=['buffered'], order='C', op_dtypes=['S']):
#     print(x) # b'1' b'2' b'3' b'4' b'5' b'6'
# for x in np.nditer(arr, flags=['buffered'], order='F', op_dtypes=['S']):
#     print(x) # b'1' b'4' b'7' b'2' b'5' b'8' b'3' b'6' b'9'

"""iteratin with scalar"""
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # 2D array
# for x in np.nditer(arr[:,::2]):
#     print(x) # 1 3 4 6 7 9

"""Enumarate Iterating"""
# arr = np.array([1, 2, 3, 4, 5]) # 1D array
# for index, x in np.ndenumerate(arr):
#     print(index, x) # (0,) 1 (1,) 2 (2,) 3 (3,) 4 (4,) 5

# arr = np.array([[1, 2, 3], [4, 5, 6]]) # 2D array
# for index, x in np.ndenumerate(arr):
#     print(index, x) # (0, 0) 1 (0, 1) 2 (0, 2) 3 (1, 0) 4 (1, 1) 5 (1, 2) 6


"""Joining NumPy Arrays"""
# arr = np.array([1, 2])
# arr2 = np.array([3, 4])
# arr3 = np.concatenate((arr,arr2)) # 1D array
# print(arr3) # [1 2 5 6 7 8]

# arr = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# arr3 = np.concatenate((arr, arr2), axis=0) # 2D array
# print(arr3) # [[1 2] [3 4] [5 6] [7 8]]

"""Joining Arrays with Stack"""

"""stack: stacks arrays in sequence depth wise (along third axis)."""
# arr = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr3 = np.stack((arr, arr2), axis=1) # 2D array
# print(arr3) # [[1 4] [2 5] [3 6]]
"""hstack: stacks arrays in sequence horizontally (column-wise)."""
# arr = np.array([1, 2, 3, 4])
# arr2 = np.array([5, 6, 7, 8])
# arr3 = np.hstack((arr,arr2))
# print(arr3) # [1 2 3 4 5 6 7 8]
"""vstack: stacks arrays in sequence vertically (row-wise)."""
# arr = np.array([1, 2, 3, 4])
# arr2 = np.array([5, 6, 7, 8])
# arr3 = np.vstack((arr, arr2))
# print(arr3) # [[1 2 3 4] [5 6 7 8]]
"""dstack: stacks arrays in sequence depth wise (along third axis)."""
# arr = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr3 = np.dstack((arr, arr2))
# print(arr3) # [[[1 4] [2 5] [3 6]]]

"""Splitting NumPy Arrays"""
# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 3) # Split the array in 3 parts
# print(newarr[0])
# print(newarr[1])
# print(newarr[2])

"""Searching Arrays"""
# arr = np.array([1, 2, 3, 4, 5, 2, 0, 2])
# x = np.where(arr == 2)
# print(x) # (array([1]),)

"""Searching for searchsorder"""
# arr = np.array([1, 2, 3, 4, 5, 6])
# x = np.searchsorted(arr, 2, side='right')
# print(x)
# x = np.searchsorted(arr, 2, side='left')
# print(x)
# x = np.searchsorted(arr, 7, side='right')
# print(x)

"""Sorting Arrays"""
# arr = np.array([[3, 2, 1], [6, 5, 4]])
# print(np.sort(arr)) # [[1 2 3] [4 5 6]]

# arr = np.array(["average", "best", "worst"])
# print(np.sort(arr))

# arr = np.array([True, False, True])
# print(np.sort(arr)) # [False  True  True]

"""filtering arrays"""

# arr = np.array([1, 2, 3, 4, 5, 6])
# filter_arr = []
# for element in arr:
#     if element > 3:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)

# newarr = arr[filter_arr]
# print(newarr) # [4 5 6]
# The above code can be simplified using numpy's built-in functions

arr = np.array([41, 42, 43, 44, 45, 46])

filter_arr = arr > 43

newarr = arr[filter_arr]
print(filter_arr) # [False False False  True  True  True]
# The above code can be simplified using numpy's built-in functions
print(newarr) # [44 45 46]


