import numpy as np

# 1. 열병합 : hstack((array1, array2)), concatenate((array1, array2), axis=1),
# column_stack((arr, arr2)), stack((arr,arr2), axis=1)

arr = np.arange(9).reshape((3, 3))
arr2 = arr * 2
print(arr)
print(arr2)
print(np.hstack((arr, arr2)))
print(np.concatenate((arr, arr2), axis=1))
print(np.column_stack((arr, arr2)))

# 2. 행병합 : vstack((array1, array2)), concatenate((array1, array2), axis=0),
# row_stack((arr, arr2)), stack((arr,arr2), axis=0)

arr = np.arange(9).reshape((3, 3))
arr2 = arr * 2
print(arr)
print(arr2)
print(np.vstack((arr, arr2)))
print(np.concatenate((arr, arr2), axis=0))
print(np.row_stack((arr, arr2)))
