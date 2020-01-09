# Numpy 모듈
# 파이썬의 리스트 업그레이드
# 벡터화 연산(행렬 연산)이 가능(요소끼리 연산 가능)
# bool 값으로 인덱싱이 가능

import numpy as np

arr = np.arange(10)  # np.arange() -> range()랑 같은 기능
print(arr)
arr = np.arange(1, 10)
print(arr)
arr = np.arange(1, 10, 2)
print(arr)
arr = np.arange(1, 10, dtype=np.float)
print(arr)
arr = np.arange(1, 10, dtype=np.float).reshape((3, 3))  # arange().reshape(튜플)로 arange를 다중차원으로 바꿀 수 있다.
print(arr)
