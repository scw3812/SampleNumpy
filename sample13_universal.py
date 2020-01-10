# 유니버설 함수 -> 요소에 적용되는 함수

import numpy as np

arr = np.array([5.4778, -2.2355, 4.2324, 9.5232, 3.0])
print("절댓값:", np.abs(arr))
print("소수점 반올림(소수점 자리 지정 가능):", np.around(arr))  # around = round
print("소수점 반올림(소수점 자리 지정 가능):", np.round(arr, 2))
print("이하의 정수값 중 가장 가까운 값:", np.floor(arr))
print("이상의 정수값 중 가장 가까운 값:", np.ceil(arr))
print("버림:", np.trunc(arr))
arr = np.array([1, 4, 9, 16, 25])
print("제곱근:", np.sqrt(arr))
