import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

ds=sb.load_dataset('tips')
print(ds)

sb.jointplot(x='tip',y='total_bill',data=ds)
plt.show()