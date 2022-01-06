color = ['빨강','노랑','파랑']
L1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
L2 = list(range(1,20,2))
student = ['20211234','홍길동','국어국문학과', 180, 70 , 4.5]


import numpy as np 
print(np.__version__)

arr = np.array([1,4,2,3,5] )
print(L1 , arr)


L2 = [3.14,4,1,0.5]
#arr2의 경우 소수점이 있는 형식의 값때문인지 소수점2자리씩이 배정된거 처럼 보인다.
arr2 = np.array([3.14,4,1,0.5])
print(L2,arr2)

#왜 type이 float64,int64이렇게 안나오고 array로 통일되서 나오지?
arr3 = np.array([1.,2.,3.,4.])
arr4= np.array([1.,2.,3.,4.], dtype = object)
arr5=np.array([1.,2.,3.,4.], dtype = int)
print(type(arr3),type(arr4),type(arr5))
print(arr3,arr4,arr5)

#얘는 잘나옴
print(arr4.dtype)
print(arr5.dtype)

L3 = list(range(0,20,2))
print(L3,'의 DATA TYPE : ',type(L3))
a3 = np.arange(0,20,2) #arrange가 아니고 a range다.
print(a3)

#list,array와 numpy의 차이는 ,가 있고 없고 차이가 보임

L4 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

for row_val in range(len(L4)):
    for col_val in range(len(L4[row_val])):
        print(L4[row_val][col_val])
        
rand1=np.random.random(5)
rand1=np.random.random((3,4))
#numpy모를땐 이 구조 이해 안됬는 데, numpy의 random함수를 써서 그렇군
#random()*5가아닌 random(5)이므로 5개짜리 배열생성

r1 = np.arange(1,10);
r2 = r1.reshape(3,3);
print(r2)

print(r1.dtype,r2.dtype)
print(r1.ndim,r2.ndim)
print(r1.shape,r2.shape)
print(r1.itemsize,r2.itemsize)

arr1 = np.zeros(5)
arr2 = np.ones(5)
print(arr)