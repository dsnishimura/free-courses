import pandas as pd

df= pd.read_csv("ex4-ds.csv",sep=';',header=None)
print(df)
df.to_html('ex-df')