# Numpy 모듈
# 파이썬의 리스트 업그레이드
# 벡터화 연산(행렬 연산)이 가능(요소끼리 연산 가능)
# bool 값으로 인덱싱이 가능

import numpy as np

arr = np.zeros(5)  # np.zeros(n) -> 실수 0 n개
print(arr)
arr = np.ones(5)  # np.ones(n) -> 실수 1 n개
print(arr)
arr = np.empty(10)  # np.empty(n) -> 임의의 실수 n개
print(arr)
arr = np.full(5, 100)  # np.full(n, a) -> a n개
print(arr)
