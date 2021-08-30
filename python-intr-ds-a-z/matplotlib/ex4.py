import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')

sweets=['milk shake','ice cream', 'chocolate', 'gum']
sales=[20,10,30,15]
colors=['white','red','brown','pink']

plt.pie(sales,labels=sweets,colors=colors)
plt.title('sweet chart')

plt.show()
