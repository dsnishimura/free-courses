import scipy as sp
import numpy as np
from scipy import linalg

var1 = np.array([[2,6],[1,5]])
var2 = np.array([[12,18],[9,13]])
f1= sp.linalg.inv(var1)

print(f1,"\n")
