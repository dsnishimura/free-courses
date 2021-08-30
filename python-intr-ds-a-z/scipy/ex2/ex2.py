import scipy as sp
import numpy as np
from scipy import fft

var1 = np.array([[2,4,6],[1,3,5]])
t1 = sp.fft.fft(var1)

print(t1,"\n")
