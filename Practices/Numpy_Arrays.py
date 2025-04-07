import numpy as np

"""Creating differents types of arrays"""

arr1D = np.array([1,2,3,4,5]) 
arr2D = np.array([[1,2,3,4,5], [6,7,8,9,10]])
arr3D = np.array([[[1,2],[3,4],[5,6]]])

"""Checking the dimensions"""
# Ndim function allow to check the dimensions on the array
print(f"The dimension of arr1D: {arr1D.ndim}")
print(f"The dimension of arr2D: {arr2D.ndim}")
print(f"The dimension of arr3D: {arr3D.ndim}")

"""Access arrays"""
print("............................................") #Space
value1 = arr1D[0]
value2 = arr2D[1,3]
value3 = arr3D[0:1]

"""Convert array data as a type"""
print("............................................") #Space
conv = np.array([1,2,3,4,5], dtype='S')
print(f"This is the value of the variable 1 to 5 convert to a string: {conv}")
newarr = conv.astype(int)
print(f"This is the value as integer: {newarr}")

"""Checking the type of a data in the array"""
print("............................................") #Space
print(f"Type of arr1D: {arr1D.dtype}")
print(f"Type of conv: {conv.dtype}")

"""Copy of an array"""
print("............................................") #Space
valueQ = np.array([1,2,3,4])
x = valueQ.copy() # This don't make changes in the original array
x[1] = 32
print(f"the value of the copy is: {x} and the original value is {valueQ}")

"""View of the array"""
print("............................................") #Space
#This makes changes in both arrays
a = np.array([1,2,3,4,5])
b = a.view()
b[0] = 23
print(f"Result of view method is {a} values from the original array,\nAnd {b} values from the b variable")

"""Checking if the array owns its values"""
print("............................................") #Space
c = np.array({1,2,4,5,6})
d = c.copy()
e = c.view()
print(f"The copy result: {d.base} \nThe view result: {e.base}")

"""Shaping an array"""
print("............................................") #Space
