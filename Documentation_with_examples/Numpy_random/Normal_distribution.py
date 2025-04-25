from numpy import random

# Generate a single random number from a normal distribution with mean 0 and standard deviation 1
# random_number = random.normal(2,3)
# print("Random number from normal distribution:", random_number)

# y = random.normal(loc=2, scale=2, size=(2,3))
# print(y)

# Example
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# sns.displot(random.normal(size=1000), kind="kde")
# plt.show()

datos = np.random.normal(loc=100, scale=50, size=1000)
sns.displot(datos, kind="kde")
plt.show()
print("Media:", np.mean(datos))
print("Desviación estándar:", np.std(datos))
print("Mediana:", np.median(datos))