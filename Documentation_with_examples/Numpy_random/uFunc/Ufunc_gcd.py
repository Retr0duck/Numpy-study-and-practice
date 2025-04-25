import numpy as np

num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is:", x)

arr = np.array([20, 8, 32, 36, 16])

y = np.gcd.reduce(arr)

print(y)
np.where(y[0])