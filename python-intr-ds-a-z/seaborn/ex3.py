import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

ds=sb.load_dataset('flights')
#print(ds)

sb.catplot(x='month',y='passengers',data=ds,kind='box')
plt.show()