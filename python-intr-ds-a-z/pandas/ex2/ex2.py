import pandas as pd

food1={'number':[1,2,3,4,5],'name':["apple","banana","peach","pizza","popcorn"], 'price':[8,3,5,10,3]}
food2={'number':[1,2,3,4,5],'name':["apple","banana","cheese","pizza","popcorn"], 'price':[2,3,5,10,3]}

ds1= pd.DataFrame(food1)
ds2 = pd.DataFrame(food2)

fusion = pd.merge(ds1,ds2,on='number')

print(fusion,'\n')
