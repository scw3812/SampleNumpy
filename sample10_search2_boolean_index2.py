# Numpy 모듈
# 파이썬의 리스트 업그레이드
# 벡터화 연산(행렬 연산)이 가능(요소끼리 연산 가능)
# bool 값으로 인덱싱이 가능 -> 불린 리스트에 저장하고 True 값과 일치되는 데이터 색인

import numpy as np

arr = np.arange(1, 16)
print("5보다 큰 3의 배수")
print(arr[(arr > 5) & (arr % 3 == 0)])

