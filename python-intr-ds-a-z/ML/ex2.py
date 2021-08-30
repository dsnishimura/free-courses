import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

candidate={'fin':[4,5,6,4,5,8,7,3,9,8,4,1,10,2,3,8,5,8,1,3,6,5,4,7,8],
        'eng':[4,5,6,4,5,8,7,3,9,8,4,1,10,2,3,8,5,8,1,3,6,5,4,7,8],
        'cs':[4,5,6,4,5,8,7,3,9,8,4,1,10,2,3,8,5,8,1,3,6,5,4,7,8],
        'g_j':[1,1,0,1,0,0,0,0,0,1,0,1,1,1,0,0,0,1,1,0,0,0,1,0,1]

}

df=pd.DataFrame(candidate,columns=['fin','eng','cs','g_j'])
#print(df)

features=list(df.columns.values)
features.remove('g_j')
x=df[features]
#print(x.head)
y= df['g_j']
print(y.head)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)

log_reg=LogisticRegression()

log_reg.fit(x_train,y_train)

y_pred=log_reg.predict(x_test)

conf_mat=pd.crosstab(y_test,y_pred,rownames=['real'],colnames=['predicted'])
sns.heatmap(conf_mat,annot=True)

print('Accuracy:',metrics.accuracy_score(y_test,y_pred))

plt.show()

