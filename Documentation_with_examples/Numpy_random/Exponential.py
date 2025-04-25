from numpy import random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x = random.exponential(scale=1.0, size=(2,3))
sns.histplot(x, bins=30, kde=True)
plt.show()