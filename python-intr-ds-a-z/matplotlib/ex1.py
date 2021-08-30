import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')

x=[2,4,6]
y=[4,8,24]

x2=[3,6,9]
y2=[10,15,20]

plt.plot(x,y)
plt.plot(x2,y2)

plt.title('test')
plt.xlabel('test X values')
plt.ylabel('test Y values')

plt.show()