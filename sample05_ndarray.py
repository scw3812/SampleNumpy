# Numpy 모듈
# 파이썬의 리스트 업그레이드
# 벡터화 연산(행렬 연산)이 가능(요소끼리 연산 가능)
# bool 값으로 인덱싱이 가능

import numpy as np

arr = np.array([[10, 20], [20, 30], [30, 40]])  # 다중 차원으로 구성할 때 안의 요소들 형태가 같으면 전부 ndarray로 바꿔주는 듯
print(arr)
print("차원:", arr.ndim)
print("차원크기:", arr.shape)  # 튜플로 반환 (1차원, 2차원, 3차원, ...)
print("타입:", arr.dtype)
