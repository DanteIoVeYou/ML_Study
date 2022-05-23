# Jupyter notebook

快捷键

- 新建cell：a、b
- 删除cell：dd、x
- 运行cell：shift+enter
- 切换cell模式：
  - m：将code模式切换到markdown
  - y：将markdown切换到code
- 智能补全：tab键
- 打开帮助文档：shift+tab



# 运算符

- 算数运算符: \+ - * / % ** // 

- 比较运算符
- 赋值运算符
- 位运算符
- 逻辑运算符:and or not
- 成员运算符: in not in
- 身份运算符: is is not



# 输入输出

- print
- 格式化输出：`print('name: '%(name))`
- input：返回的是字符串类型的数据
- id打印内存地址
- 强制类型转换
- 数学计算：abs、log
- pi、e
- type查看数据类型



# 字符串

- 字符串类型数据：单引号、双引号括起来

- 通过索引取值

- 切片：字符串变量名[0:4]

- \+拼接

- *重叠拼接

- \n \t

- 原始形式输出：r'\t \n' 

- find：找到返回位置；找不到返回-1

- replace：不会替换原始字符串，而是返回一个新字符串

- upper

- lower

- strip：去掉字符串前后的回车

- ```python
  str.split(sep=None, maxsplit=-1)
  ```

- startswith：是否以xxx开头

- 字符串是不可变类型



# 列表

一个有序的可重复的元素集合，可嵌套、迭代、修改、分片、追加、删除、成员判断

- 不同类型数据可以存储到列表中

- 索引

- 切片

- 连续的内存空间

- 列表里存的是地址

- 本质是指针数组

- 可变类型数据

- append：将一个元素添加到列表末尾

- insert：将元素添加到列表指定位置

- pop：将列表中指定的元素取出 ```pop(index=-1, /)```

- remove

- del

- \+

- *

- in

- for in

- sort：基于原始列表进行排序

- count：某个元素在列表中出现的次数

- extend

- clear

- copy：只能拷贝列表的第一层，即浅拷贝

- 深拷贝

  ```py
  import copy
  copy.deepcopy()
  ```

  

  



## 内置函数

- len
- max
- min
- list(seq)：将序列转换成列表
- sorted：将排序后的结果重新返回到一个新列表中，不会影响原来的列表



## 字符串转列表

```python
s = 'hello world hello'
result = s.split(' ')
print(result)
```

## 列表转字符串

```python
l = ['hello', 'world', 'hello']
result = ' '.join(l)
print(result)
```





# 元组

元组是不可变序列

- 小括号括起来
- 可以嵌套
- \+
- *
- len
- 只能保证一级子序列不可被修改



# 字典

基于哈希散列算法实现的
- items()：返回字典中所有的元素
- keys()：返回字典中所有的key值
- values()：返回字典中的所有value值
- pop(key)：取出之后字典里就没有这个键值对了
- popitem()：去除最后一个键值对并删除
- update()：将dict2的键值对添加到dict1的末尾

# bytes
二进制类型
- `b = b'hello'`
- decode()：将二进制类型的数据转换成字符串类型的数据
- encode()：将字符串类型的数据转换成二进制类型的数据

# set
集合是一个无序不重复元素的容器，集合数据类型的核心作用在于自动去重
- []：不能通过下标访问元素
- add()
- update()：将一个对象更新到已有的集合中，也会自动去重
- remove()
- pop()

# 流程控制
## 顺序
## 选择
- if
- elif
- else
## 循环
- while
- while else 循环正常结束，else才会执行
- for：for i in 字符串|列表|元组|字典|集合
- for key,value in dict.items() 
- for else

# random
随机生成数字
```python
import random
# 随机生成1-100的数字
num = int(random.random()*100)
```

# 函数
- 必须要有return， 不写返回None
- 内部函数
- 动态参数


```python
def func(*args):
  print(args)
  print(*args)
t = (1,2,3)
func(t)
func(*t)
```

```python
def func(**kwargs):
  print(kwargs)
func(k1=1,k2=2,k3=3)
```
- 作用域
- global：引用外部的全局变量


# range()函数

```python
for i in range(1,5):
  print(i)
```

# lambda表达式
```lambda
result = lambda x:1 if x > 0 else 0 
```
 # 递归