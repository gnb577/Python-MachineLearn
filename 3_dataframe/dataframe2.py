import numpy as np
import pandas as pd

data1 = {'AAA' : {'a' : 4,'b':5, 'c':6, 'd':7}, 
        'BBB' : {'a': 10, 'b' : 20, 'c':30, 'd': 40},
        'CCC' : {'a':100, 'b': 50, 'c': -30, 'd': -50} }
print(data1,'\n')


data2 = {'AAA' : {'a' : 4,'b':5, 'c':6, 'd':7}, 
        'BBB' : {'a': 10,  'c':30, 'd': 40},
        'CCC' : {'a':100, 'b': 50, 'd': -50} }
print(data1,'\n')


df1 = pd.DataFrame(data1)
print(df1,'\n')

df2 = pd.DataFrame(data2)
print(df2,'\n')

#골라 뽑기도 가능
df3 = pd.DataFrame(data2,columns=['AAA','CCC'],index=['a','c'])
print(df3,'\n')