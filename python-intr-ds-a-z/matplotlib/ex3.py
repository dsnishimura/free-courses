import matplotlib.pyplot as plt
from matplotlib import style

style.use('bmh')

num=[1,20,30,35,45,65,74,83,91,15,25,36,95,64,12,18,29,31,73]
jmp=[0,15,30,45,60,75,90,105]

plt.title('test 1 hist')
plt.xlabel('test x')
plt.ylabel('test y')

plt.hist(num,jmp,histtype='step')

plt.show()