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
arr = np.arange(12).reshape((3, 4))
print("1차원", arr.flatten())  # flatten()으로 1차원으로 바꿀 수 있다.
print("1차원", arr.ravel())  # ravel()도 가능

arr = np.array([8, 54, 22, 456])
print("최솟값:", np.min(arr))  # buitin이랑 기능 차이가 있나?
print("최댓값:", np.max(arr))
print("최솟값 위치:", np.argmin(arr))
print("최댓값 위치:", np.argmax(arr))

arr = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3]) * 2
print("더하기", np.add(arr, arr2), arr + arr2)
print("빼기", np.subtract(arr, arr2), arr - arr2)
print("곱하기", np.multiply(arr, arr2), arr * arr2)
print("나누기", np.divide(arr, arr2), arr / arr2)
print("몫", np.floor_divide(arr, arr2), arr // arr2)
print("나머지", np.mod(arr, arr2), arr % arr2)

arr = np.array([11, 2, 3, 4])
arr2 = np.array([1, 22, 33, 44])
print("arr>arr2", np.greater(arr, arr2))
print("arr>=arr2", np.greater_equal(arr, arr2))
print("arr<arr2", np.less(arr, arr2))
print("arr<=arr2", np.less_equal(arr, arr2))
print("arr==arr2", np.equal(arr, arr2))
print("arr!=arr2", np.not_equal(arr, arr2))
print("각 요소별 큰 값:", np.maximum(arr, arr2))
print("각 요소별 작은 값:", np.minimum(arr, arr2))
