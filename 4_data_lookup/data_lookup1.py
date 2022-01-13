import pandas as pd
import seaborn as sns
import numpy as np

s1 = [1,2,3,4]
s2 = ['a','b','c','d']

df = pd.DataFrame({'a1':s1,'a2':s2})
df.index=['w','x','y','z']
print(df,'\n')
print(df['a1'],'\n')

#key값은 속성명으로 쓰이고
#value값은 row로 쓰인다고 보면 될듯

#loc함수는 인덱스명으로 검색
df_loc1=df.loc['x']
df_loc2=df[0:2]
print(df_loc1,'\n')
print(df_loc2,'\n')

df_loc3=df.loc['w']
df_loc3=df.loc['w':'y']
print(df_loc3,'\n')


#iloc는 인덱스 행번호로 탐색
df_iloc1=df.iloc[0:2]
df_iloc2=df.iloc[-1]
print(df_iloc1,'\n')
print(df_iloc2,'\n')