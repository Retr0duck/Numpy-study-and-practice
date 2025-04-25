from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = sns.displot(random.chisquare(df=1, size=1000), kind="kde")

plt.show(x)