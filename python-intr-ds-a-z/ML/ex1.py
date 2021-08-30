import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,6,7,78,9,64,12,15,36,39,56,89])
y=np.array([10,26,93,54,66,77,78,93,11,13,5,91,45,61,99])
f1=np.polyfit(x,y,1)

plt.plot(x,np.polyval(f1,x),'r-')
plt.show()
print(f1)