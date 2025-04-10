from numpy import random

# Generate a 1D array with 100 values 
a = random.choice([3,5,7,9], p=[0.1, 0.3, 0.6, 0.0], size=100)
print(a)
# The sum of all the probabilities is 1.0

b = random.choice([3,5,7,9], p=[0.1, 0.3, 0.6, 0.0], size=(3,5))
print(b)
# The sum of all the probabilities is 1.0