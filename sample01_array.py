# Numpy 모듈
# 파이썬의 리스트 업그레이드
# 벡터화 연산(행렬 연산)이 가능(요소끼리 연산 가능)
# bool 값으로 인덱싱이 가능

import numpy as np

m = [10, 20, 30]
print(m*2)  # [10, 20, 30, 10, 20, 30]

# array 생성
arr = np.array(m)  # np.array(list) -> ndarray 오브젝트 반환 [10 20 30](쉼표가 없음)
print(arr, type(arr))

# array는 자동으로 요소에서 가장 큰 타입으로 upcasting 됨(작은타입 -> 큰타입)
m = [10., 20, 30]
print(np.array(m))  # [10. 20. 30.] 실수형으로
