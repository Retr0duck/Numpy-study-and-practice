# Multinomial Distribution Example
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
# Plotting the results
sns.histplot(x, bins=30)
plt.show()