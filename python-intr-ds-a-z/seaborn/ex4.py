import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
ds=sns.load_dataset('tips')
print(ds)

plot=sns.FacetGrid(ds,col='sex',hue='smoker')
plot.map(plt.scatter,'total_bill','tip')
plot.add_legend()


plt.show()