import pandas as pd

import numpy as np

s1 = [1,2,3,4]
s2 = ['a','b','c','d']

df = pd.DataFrame({'a1':s1,'a2':s2,'a3':s1})
df.index=['w','x','y','z']
print(df,'\n')

df_loc1=df.loc['w', 'a1':'a2']
print(df_loc1,'\n')
df_loc2=df.iloc[0:2, 0:3]
print(df_loc2,'\n')