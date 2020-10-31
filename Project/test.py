from numpy import random
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import seaborn as sns
from Distribuicoes import *


#Plot aos graficos com a funcao implementada
a =[]
for i in range(100000):
    a.append(uniformeDisc(0, 3))
    #print(a[i])


ax = sns.distplot(a , hist=True)
ax.yaxis.set_major_formatter(PercentFormatter())
plt.show()

