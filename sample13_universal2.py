# 유니버설 함수 -> 요소에 적용되는 함수

import numpy as np

arr = np.array([1, 2, 3, 4])
print("요소 전체 곱:", np.prod(arr))
arr = np.array([[1, 2], [3, 4], [5, 6]])
print("2차원 배열 행 요소 전체 곱:", np.prod(arr, axis=0))  # 1행 * 2행 * 3행
print("2차원 배열 열 요소 전체 곱:", np.prod(arr, axis=1))   # 1열 * 2열
arr = np.array([[1, 2], [3, np.nan]])  # nan(not a number) -> nan을 포함한 연산하면 nan이 나옴
print("nan 포함 곱 연산:", np.nanprod(arr, axis=1))  # nanprod(arr) : nan을 1로 바꿔서 연산해줌
arr = np.array([[1, 2], [3, 4], [5, 6]])
print("누적 연산:", np.cumprod(arr, axis=1))  # -> 연산 과정을 열별로 반환 -> 1열 2열 ...
print("누적 연산:", np.cumprod(arr, axis=0))  # -> 연산 과정을 행별로 반환 -> 1행 2행 ...

arr = np.array([1, 2, 3, 4])
print("요소 전체 합:", np.sum(arr))
print("요소 전체 합:", np.sum(arr, keepdims=True))  # keepdims=True이면 차원을 유지해줌(리스트로 반환)
arr = np.array([[1, 2], [3, 4], [5, 6]])
print("2차원 배열 행 요소 전체 합:", np.sum(arr, axis=0))
print("2차원 배열 열 요소 전체 합:", np.sum(arr, axis=1))
arr = np.array([[1, 2], [3, np.nan]])
print("nan 포함 곱 연산:", np.nansum(arr, axis=1))  # nansum(arr) -> nan을 0으로 바꿔서 연산
arr = np.array([[1, 2], [3, 4], [5, 6]])
print("누적 연산:", np.cumsum(arr, axis=1))
print("누적 연산:", np.cumsum(arr, axis=0))

arr = np.array([1, 2, 4, 7, 12])
print("차분:", np.diff(arr))  # 뒤 인덱스에서 앞 인덱스를 뺀 값을 리스트로 반환
print("2번 차분:", np.diff(arr, 2))
arr = np.array([[1, 2], [3, 4], [5, 6]])
print("2차원 배열 요소 차분:", np.diff(arr))  # = 열 차분
print("2차원 배열 행 요소 차분:", np.diff(arr, axis=0))
print("2차원 배열 열 요소 차분:", np.diff(arr, axis=1))
