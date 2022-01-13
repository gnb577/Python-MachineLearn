import numpy as np
import pandas as pd

np1=np.array([[1,2,3],[4,5,6],[7,8,9],['a','b','c']])
np2=np.array([[1,2,3],[4,5,6],[7,8,9]])

df_arr = pd.DataFrame(np2)

#series는 index 대신 name인거 같다.
s1 = pd.Series([1,2,3,4])
s2 = pd.Series(['a','b','c','d'])
s3 = pd.Series([9,8,7,6],name='s3')
s4 = pd.Series(['가', '나', '다'],name='s4')

df1 = pd.DataFrame([s1,s2])
print(df1.values,'\n')
print(df1.columns,'\n')
print(df1.axes,'\n')
print(df1.shape,'\n')


data = {
        '교과목명' :  {'S001':'python','S002':'Excel응용', 'S003':'Database', 'S004':'컴퓨팅적사고'},
        '학점' :  {'S001': 3,'S002':2, 'S003':3, 'S004':1},
        '수강대상' : {'S001': '국문','S002':'불문', 'S003':'영문', 'S004':'영문'} 
       }

df = pd.DataFrame(data)
print(df)


# 시리즈 형식
학수번호 = pd.Series(['S001','S002','S003','S004'])
교과목명 = pd.Series(['python','Excel응용','Database','컴퓨팅적사고'])
학점 = pd.Series([3,2,3,1])
학점2 = [3,2,3,1]
수강대상 = pd.Series(['국문','불문','영문','영문'])

#이거랑 비슷한 형식을 써서 python 3 국문이렇게 쓰고 싶은데
수강신청 = pd.DataFrame({'교과목명':교과목명,'학점':학점2,'수강대상':수강대상},index=학수번호)
print(수강신청,'\n')
# series는 한몸이라 안 되나본데...