import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

ds=sb.load_dataset('dots')
#print(ds)

sb.distplot(ds['time'])
plt.show()

