import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')

x=[3,6,7,9,10]
y=[5,10,15,25,30]

plt.title('ex5 plot')
plt.xlabel('test x')
plt.ylabel('test y')

plt.scatter(x,y)

plt.show()