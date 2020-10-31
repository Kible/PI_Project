from numpy import random
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import seaborn as sns
from Distribuicoes import *


#Plot aos graficos com a funcao implementada
a =[]
for i in range(1000):
    a.append(binomial(5, 0.5))
    print(a[i])


ax = sns.distplot(a , hist=True)
ax.yaxis.set_major_formatter(PercentFormatter())
plt.show()

