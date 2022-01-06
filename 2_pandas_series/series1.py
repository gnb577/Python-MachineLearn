import pandas as pd
d = {'a':1,'b':2,'c':3} #'key'로 사용하네...
print(d,d['a'],type(d))

s1 = pd.Series(data = d)
print(s1)
print()
s2= pd.Series([9,8,7]) #key value형태가 아니면 자동으로 인덱스 붙여줌
print(s2)
print()
s3= pd.Series([9,8,7], index=['x','y','z'])
print(s3)
print(s3[2],s3['y'])
print()
s4= pd.Series(data=[9,8,7], index=['x','y','z'])
s5= pd.Series(data=[9,8,7], index= list('123'))
print(s5['1':'2']) #key~key까지도 가능하네...
