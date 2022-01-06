import pandas as pd
import numpy as np

L1 = [4,1,6,3,9,5,11]
s1 = pd.Series(L1,index=list('abcdefg'))
print(s1,'\n')
s1.index=list('hijklmn')
print(s1,'\n')

dict = {'a':1,'b':2,'c':3}
s2 = pd.Series(dict)