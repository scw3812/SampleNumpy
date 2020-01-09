# Numpy 모듈
# 파이썬의 리스트 업그레이드
# 벡터화 연산(행렬 연산)이 가능(요소끼리 연산 가능)
# bool 값으로 인덱싱이 가능

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("첫번째", arr[0])
print("마지막", arr[-1])
print("1~5", arr[0:5])
print("거꾸로", arr[::-1])

arr.shape = (2, 5)
print("다중차원 표현", arr[0, 1:])  # [n차원, n-1차원,...,1차원]으로 다중차원 인덱싱 가능
print("전체 행 첫번째 값", arr[:, 0])  # [:][] 이걸로 쓰면 앞 인덱싱이 리스트를 반환 해 리스트에서 인덱싱을 함(리스트 개념) -> 리스트 반환
# [,]는 행렬 느낌, [][]는 2차원 리스트 느낌
print(arr[0][[0, 2, 4]])  # fancy 색인 : array는 [리스트]로 여러 값을 한꺼번에 인덱싱해 array로 반환 가능
print("전체 행 첫번째, 세번째, 다섯번째", arr[:, [0, 2, 4]])
print("전체 행 두번째~끝까지 값", arr[:, 1:])
print("1행 2행 두번째~끝까지 값", arr[:2, 1:])
