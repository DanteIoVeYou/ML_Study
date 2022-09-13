# numpy处理数值型数据，pandas处理字符串、时间序列等数据
# pandas两个常用类
# - Series
# - DataFrame

# Series由values和index组成
# Series由列表、numpy数组、字典创建
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
# 使用numpy数组或者列表充当数据源
s1 = Series(data=['张三', '李四', '王五'])
print(s1)
s2 = Series(data=np.random.randint(0,100,size=(5)))
print(s2)
# 字典作为数据源
dic = {
    '语文': 100,
    '数学': 100,
    '英语': 101,
}
s3 = Series(data=dic)
print(s3)
s4 = Series(data=[100, 99, 98], index=['语文', '数学', '英语'])
print(s4)
# 显示索引不会覆盖隐式索引
s5 = Series(data=np.linspace(0, 10, 5), index=['a', 'b', 'c', 'd', 'e'])
print(s5)
print(s5[0])
print(s5.a)
print(s5[0:5])
print(s5['a':'e'])
print(s5.dtype)
print(s5.values)
print(s5.index)
print(s5.head(3))
print(s5.unique())
print(s5.nunique()) # 返回去重后元素的个数
print(s5.value_counts())
s6 = Series([1,2,3])
s7 = Series([4,5,6,7])
s8 = s6 + s7
print(s8)
print(s8.isnull())
print(s8.notnull())
# 将Series中的空值进行过滤
# bool值可以作为Series的索引
print(s8[s8.notnull()])
print(s8.sum())
# ~取反运算符
print(s8[~s8.notnull()])
# NaN可以参加运算
print(s8[~s8.notnull()].sum())

# DataFrame是一个表格型的数据
df1 = DataFrame(data=np.random.randint(0,100,size=(4,5)))
print(df1)
dic = {
    'name': ['张三', '李四', '王五'],
    'salary': [10000,20000,30000],
}
df2 = DataFrame(data=dic, index=['a', 'b', 'c'])
print(df2)
# index设置行索引
# columns设置列索引
df3 = DataFrame(data=[[1,2,3], [4,5,6], [7,8,9]], index=['a', 'b', 'c'], columns=['甲', '乙', '丙'])
print(df3)

dic = {
    '张三': [100,100,100],
    '李四': [60,60,60],
}
df4 = DataFrame(data=dic, index=['语文', '数学', '英语'])
print(df4)

df5 = DataFrame(np.random.randint(0,100,size=(6,8)))
print(df5)
print(df5[0]) # 取单列
print(df5.iloc[0]) # 取行
# loc后面跟显示索引，iloc后面跟隐式索引
print(df4.iloc[0])
print(df4.loc['语文'])
print(df5.iloc[[1,2,3], 5])
print(df5[0:3]) # 切片是行切片
print(df5.iloc[:,0:3]) # 列切片

# DataFrame的运算
