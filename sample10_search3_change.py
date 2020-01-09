import numpy as np

arr = np.arange(1, 11)
arr2 = arr.copy()  # 깊은 복사
arr[arr % 2 == 0] = 2
print(arr)
arr[1:5] = 1000
print(arr)

print(arr2)

m = [1, 2, 3, 4, 5]
m2 = m[:3]  # 깊은 복사 -> 새 리스트 만듬 -> 성능이 떨어짐
print(m, m2)
m2[0] = 100
print(m, m2)

m2 = np.array(m)
m3 = m2[:3]  # array는 슬라이싱하면 얕은 복사됨 -> 같은 주소 참조 -> 성능이 좋음
m3[0] = 100
print(m2, m3)

