import matplotlib.pyplot as plt
from matplotlib import style

style.use('bmh')

x1=[2,4,6]
y1=[4,8,24]

x2=[3,6,9]
y2=[10,15,20]

x3=[5,10,15]
y3=[9,18,27]


plt.bar(x1,y1)
plt.bar(x2,y2)
plt.bar(x3,y3)

plt.title('test')
plt.xlabel('test X values')
plt.ylabel('test Y values')

plt.show()