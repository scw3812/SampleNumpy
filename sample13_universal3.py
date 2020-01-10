# 유니버설 함수 -> 요소에 적용되는 함수

import numpy as np

arr = np.array([[1, 2, 1, 2], [3, 4, 4, 6], [5, 6, 8, 10]])
print("부분 합(1행 2행):", np.sum(arr[:2], axis=1))
print("부분 합(1열 3열):", np.sum(arr[:, [0, 2]], axis=0))

arr = np.arange(1, 11)
print("평균:", np.mean(arr))

arr = np.array([7, 4, 79, 98, 12, 3])
arr2 = np.sort(arr)  # sorted(array) -> array가 아니라 리스트가 반환됨, np.sort(arr) -> array 반환
print(arr, arr2)
arr.sort()  # array는 sort()를 쓸 수 있지만 reverse 인자를 넣을 수 없다
print(arr[::-1])

arr = np.arange(12)
print("1차원", arr)
arr.shape = (3, 4)
print("2차원", arr)

print("1차원", arr)
