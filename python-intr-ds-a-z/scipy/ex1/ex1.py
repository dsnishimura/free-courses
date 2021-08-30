import scipy as sp
from scipy import integrate

var1 = lambda y, x: x*y**8
f1=integrate.dblquad(var1,0,6,lambda x:0, lambda x:1)

print(f1,"\n")


