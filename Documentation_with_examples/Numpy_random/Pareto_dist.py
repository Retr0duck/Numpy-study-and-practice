from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.pareto(a=2, size=1000))

plt.show()