import numpy as np

# 1. 열분할 : 세로로 분할 -> np.hsplit(array, 분할 개수), np.split(array, 분할개수, axis=1)
arr = np.arange(12).reshape((3, 4))
print(arr)
arr1 = np.hsplit(arr, 2)
print(arr1)
x, y = arr1
print(x)
arr2 = np.split(arr, 2, axis=1)
print(arr2)

# 2. 행분할 : np.vsplit(array, 분할 개수), np.split(array, 분할개수, axis=0)
arr = np.arange(12).reshape((4, 3))
print(arr)
arr3 = np.vsplit(arr, 2)
print(arr3)
x, y = arr3
print(x)
arr4 = np.split(arr, 2, axis=0)
print(arr4)

# 실습 홀수끼리, 짝수끼리 묶고 분할
# t = arr[:][1].copy()
# arr[:][1] = arr[:][2]
# arr[:][2] = t
arr = arr[[0, 2, 1, 3]]
arr5 = np.vsplit(arr, 2)
print(arr5)

arr = np.arange(12).reshape((3, 4))
print(arr)
arr6 = np.hsplit(arr[:, [0, 2, 1, 3]], 2)
print(arr6)

