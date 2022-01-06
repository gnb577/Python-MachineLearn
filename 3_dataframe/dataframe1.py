import numpy as np
import pandas as pd

d = {'col1':[1,2],'col2':[3,4]}
df = pd.DataFrame(data=d)
print(df,'\n')

df2 = pd.DataFrame([1,2,3,4,5,6,7,8])
df3 = pd.DataFrame([[1,2,3,4],[5,6,7,8]])
print(df2,'\n')
print(df3,'\n')

df4 = pd.DataFrame([[1,2,3,4],[5,6,7,8]],
                   index=list('ab'),
                   columns=list('opqr'))
                
            
print(df4,'\n')

s1 = [1,2,3,4]
s2= ['a','b','c','d']

df_lst1=pd.DataFrame([s1,s2], 
                     index=list('ab'),
                   columns=list('opqr'))
print(df_lst1,'\n')


col1=['가','나','다']
row1=['x','y','z','w']
value1 = [[1,2,3],[4,5,6],[7,8,9],[1,3,5]]


df_lst2 = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9],[1,3,5]],
                       columns=col1,
                       index=row1)
print(df_lst2,'\n')
print(df_lst2,'\n')