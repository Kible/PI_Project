from numpy import random
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import seaborn as sns
from Distribuicoes import *


#Plot aos graficos com a funcao implementada
a =[]
sample_size = 10000
for i in range(sample_size):
    a.append(uniformeDisc(0, 3))
    #print(a[i])

ax = sns.displot(a, shrink=.2)
#ax.yaxis.set_major_formatter(PercentFormatter(sample_size))
plt.show()

