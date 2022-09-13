import numpy as np
import matplotlib.pyplot as plt

arr1 = np.array([1,2,3,4,5])
print(arr1)

arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

arr3 = np.array([1, 1.1])
print(arr3)

img = plt.imread("img1.jpg")

# ones()
a1 = np.ones(shape=(3, 4, 5), dtype='str')
print(a1)

# linespace()

a2 = np.linspace(1, 100, num=10)
print(a2)

# arange()
a3 = np.arange(0, 20, step=6)
print(a3)

# random.randint
a4 = np.random.randint(0, 100, size=(3,5))
print(a4)

# random.random
a5 = np.random.random(size=(4,5))
print(a5)
# shape
# ndim
# size
# dtype
print(a5.shape)
print(a5.ndim)
print(a5.size)
print(a5.dtype)

arr = np.array([1,2,3,4,5], dtype='int')
# astype会返回一个新的数组
arrr = arr.astype(dtype='int8')
print(arrr.dtype)
# ndarray
print(type(arr))
# 索引和切片

arr = np.random.randint(0, 100, size=(4,5))
print(arr)
print(arr[1][1])

arr = np.random.randint(0, 100, size=(5,6))
print(arr)
print(arr[0:3]) # 行
print(arr[:, 0:3]) # 列
print(arr[0:3, 0:2])

# 将一维变二维 reshape()
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr)
arr = arr.reshape((3,3))
print(arr)

# 级联：将一个或多个数组进行横向或者纵向的拼接

arr1 = np.random.randint(0, 100, size=(3,4))
arr2 = np.random.randint(0, 100, size=(2,4))
# 匹配级联
arr3 = np.concatenate((arr1, arr2, arr1), axis=0) # axis 0 为纵向，1位横向
print(arr3)
# 不匹配级联：级联的数组要保证行或列的数量是一致的
# arr3 = np.concatenate((arr1, arr2, arr1), axis=1) # axis 0 为纵向，1位横向

# amin(), ptp(), mean()
arr = np.random.randint(0,100,size=(3,3))
print(arr)
print(arr.T) # 转置
