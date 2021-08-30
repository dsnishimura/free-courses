import pandas as pd

food1={'number':[1,2,3,4,5],'name':["apple","banana","lemon","chocolate","popcorn"], 'price':[8,3,5,10,3]}
food2={'color':["red","yellow","green","brown","white"],'weight':[100,150,200,175,225], 'qt':[1,2,1,3,3]}

df1=pd.DataFrame(food1)
df2=pd.DataFrame(food2)

finaldf = df1.join(df2)

print(finaldf,"\n")