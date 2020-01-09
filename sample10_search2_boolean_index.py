# Numpy 모듈
# 파이썬의 리스트 업그레이드
# 벡터화 연산(행렬 연산)이 가능(요소끼리 연산 가능)
# bool 값으로 인덱싱이 가능 -> 불린 리스트에 저장하고 True 값과 일치되는 데이터 색인

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
bool_arr = [True, False, True, False, True, True, True, True, False, False]
print(arr[bool_arr])

arr = np.arange(1, 11)
print("1. 짝수값만 출력하시오")
print(arr[arr % 2 == 0])

print("2. 5보다 큰 값만 출력")
print(arr[arr > 5])

print("3. 정조만 출력")
arr = ["홍길동", "정조", "영조", "박혁거세", "정조"]
# 기존 방법 : list_arr = [x for x in arr if x == "정조"]
arr = np.array(arr)
print(arr[arr == "정조"])
