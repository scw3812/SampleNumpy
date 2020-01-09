# Numpy 모듈
# 파이썬의 리스트 업그레이드
# 벡터화 연산(행렬 연산)이 가능(요소끼리 연산 가능)
# bool 값으로 인덱싱이 가능

import numpy as np

# 산술 연산
arr = np.array([10, 20, 30])
print(arr)
arr2 = arr*2
print(arr2)
print(arr + arr2)
print(arr * arr2)

# 비교 연산
print(arr % 2 == 0)
print(arr > arr2)
