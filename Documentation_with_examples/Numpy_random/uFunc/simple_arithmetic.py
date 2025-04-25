import numpy as np

# Addition
arr1 = np.array([10, 12, 22, 25, 30])
arr2 = np.array([10,22, 30, 25, 20])
arr_sum = np.add(arr1, arr2)
print(arr_sum)
# Output: [20 34 52 50 50]

#Subtraction
arr_1 = np.array([10, 12, 22, 25, 30])
arr_2 = np.array([10, 22, 30, 25, 20])
arr_sub = np.subtract(arr_1, arr_2)
print(arr_sub)
# Output: [ 0 -10 -8  0 10]

#Multiplication
arr_1 = np.array([10, 12, 22, 25, 30])
arr_2 = np.array([10, 22, 30, 25, 20])
arr_mul = np.multiply(arr_1, arr_2)
print(arr_mul)
# Output: [ 100 264 660 625 600]

#Division
arr_1 = np.array([10, 12, 22, 25, 30])
arr_2 = np.array([10, 22, 30, 25, 20])
arr_div = np.divide(arr_1, arr_2)
print(arr_div)

# Power
arr_1 = np.array([10, 12, 22, 25, 30])
arr_2 = np.array([10, 22, 30, 25, 20])
arr_pow = np.power(arr_1, arr_2)
print(arr_pow)


# Rest of the operations
arr1 = np.array([10, 12, 22, 25, 30])
arr2 = np.array([10, 22, 30, 25, 20])
arr_mod = np.mod(arr1, arr2)
print("mod:", arr_mod)
arr_remainder = np.remainder(arr1, arr2)
print("remainder:", arr_remainder)
arr_floordiv = np.floor_divide(arr1, arr2)

# Divmod    
arr_di = np.array([1,4,6,8,10])
arr_do = np.array([2,3,4,5,6])

arr_divmod = np.divmod(arr_di, arr_do)
print("divmod:", arr_divmod)

# Absolute 

arr_abs = np.abs(arr1)
print("absolute:", arr_abs)