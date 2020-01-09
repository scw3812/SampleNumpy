# Numpy 모듈
# 파이썬의 리스트 업그레이드
# 벡터화 연산(행렬 연산)이 가능(요소끼리 연산 가능)
# bool 값으로 인덱싱이 가능

import numpy as np

random_value = np.random.random(5)  # random(n) -> [0,1) 랜덤 n개를 array로
print(random_value)

random_value = np.random.randint(1, 5, 4)  # randint(a, b, n) -> [a,b) 랜덤 정수 n개를 array로
print(random_value)

random_value = np.random.randn(5)  # randn() -> 평균 0, 표준편차 1 정규분포에서의 랜덤 값을 n개의 array로
print(random_value)

random_value = np.random.rand(5)  # rand()
print(random_value)
