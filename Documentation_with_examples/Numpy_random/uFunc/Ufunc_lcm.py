import numpy as np

num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print("lcm of 4 and 6 is:", x)

arr = np.array([3,6,9])
y = np.lcm.reduce(arr)
print(y)

arrR = np.arange(1,11)
i = np.lcm.reduce(arrR)
print(i)