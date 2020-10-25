from numpy import random
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import seaborn as sns
import Rabbit


#Plot aos graficos com a funcao do numpy
#x = random.normal(loc=500, scale=20, size=1000)
#sns.distplot(x , hist=False)
#plt.show()



#Plot aos graficos com a funcao implementada
a =[]
for i in range(1000):
    a.append(Rabbit.normal(500, 20))


ax = sns.distplot(a , hist=True)
ax.yaxis.set_major_formatter(PercentFormatter())
plt.show()

