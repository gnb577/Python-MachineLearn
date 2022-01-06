import numpy as np 

L1 = [10,5,3,7,1,5]
L2 = [1,2,3,4,5,6]

print(L1 + L2)
#나머지 + - * / 어림도 없음

#but numpy는 산술연산이 가능함

arr1 = np.array([10,5,3,7,1,5])
arr2 = np.array([1,2,3,4,5,6])
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)

#처리속도 numpy >> python