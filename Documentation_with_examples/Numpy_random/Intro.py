from numpy import random
# Generate a random number between 0 and 100
a = random.randint(100)
print("This is a random number:")
print(a)
# Generate a random float 
print("This is a random float:")
b = random.rand()
print(b)

# Generate a random 1D array of 5 random numbers
c = random.randint(100, size=5)
print("This is a 1D array of random numbers:")
print(c)

d = random.randint(100, size=(3, 5))
print("This is a 2D array of random numbers:")
print(d)

# Generate a random 3D array of random numbers
# The shape of the array is (3, 5, 2) 
e = random.randint(100, size=(3, 5, 2))
print("This is a 3D array of random numbers:")
print(e)

# Generate a random 1D array of 5 random floats
f = random.rand(5)
print("This is a 1D array of random floats:")
print(f)

# Generate a random 2D arrya with 3 rows each with 5 random numbers
g = random.rand(3, 5)
print("This is a 2D array of random floats:")
print(g)

"""Generate Random Number from array"""
# The choice method allows you to generate a random number based on the value of the array
# The choice() method takes an array as a parameter and randomly returns one of the values.
h = random.choice([1, 2, 3, 4, 5]) #This return a random number from the array

# Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):
i = random.choice([3, 5, 7, 9], size=(3, 5))
print("This is a random number from the array:")
print(i)
# The choice method allows you to generate a random number based on the value of the array
# The choice() method takes an array as a parameter and randomly returns one of the values.