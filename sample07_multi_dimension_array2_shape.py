# Numpy 모듈
# 파이썬의 리스트 업그레이드
# 벡터화 연산(행렬 연산)이 가능(요소끼리 연산 가능)
# bool 값으로 인덱싱이 가능

import numpy as np

m = [1, 2, 3, 4, 5, 6, 7, 8]
arr = np.array(m)
arr.shape = (2, 4)  # shape에 튜플을 넣어서 차원 변경 가능
print(arr, type(arr))
