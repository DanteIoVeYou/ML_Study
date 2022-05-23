# 文件操作
## open
- 文件名
- 打开方式
- 返回文件描述符、文件句柄

- r 只读 
- w 只写：文件不存在，创建；存在，清空
- a 追加：文件不存在，创建；存在，最后追加
- x 新建：存在，报错；不存在，新建并写入
- b 二进制模式：rb wb ab
- \+ 读写模式：r+ w+ a+

## write
写完之后需要close
## close
关闭文件，数据才能保存
## tell
返回文件指针当前的位置

## seek
f.seek(offset, from_what)

## with as关键字
不需要close手动关闭
```python
with open() as fp:
    fp.write()
```

# pymysql数据库操作

## 连接
```python
conn = pymysql.Connect(
    host = '127.0.0.1',
    port = 3306,
    user = '',
    password = '',
    db = '',
    charset = 'utf8',
)
```

## 创建游标对象用来执行sql语句
```python
cursor = conn.cursor()
```

## 通过创建好的游标对象执行sql语句
```python
sql = ''
cursor.execute(sql)
```
## 事务的处理
```python
conn.commit()
```

# 模块
- 解释器内建模块
- python标准库
- 第三方模块
- 应用程序自定义模块

> import 在执行模块中所有的代码
 ## 导入模块
> 能使用模块内的所有方法
```python
import time
time.sleep(1)
```
 ## 导入模块内的某个方法
 > 想用其他方法还得继续import
 ```python
from time import sleep
sleep(1)
 ```

 ## 自定义模块
 > 文件add_module.py
 ```python
def add(x, y):
    return x + y
```

> 文件main.py
```python
import add_module
print(add_module.add(1,2))
```

# 包

> 有```__init__.py```的目录

# 常见模块

## time

- time.time()：返回时间戳
- time.strftime("%Y\%m\%d-%w")：把时间戳转换为可视化的时间
- time.sleep()：睡眠

## random
 - random.choice(列表名)：从列表中随机选出一个值
 - random.randrange(x,y)
 - random.sample(list, n)：列表中随机n个元素随机组合
 - random.shuffle(list)：将原始列表打乱
 - 

## os
- getcwd()
- makedirs()
- removedirs() 
- listdir()
- rename('oldname','newname')
- system

# 程序执行入口
> 只要在某一个文件中出现下列代码，说明这是程序入口
```python
if __name__ == '__main__':
    pass
```
> __name__指的是模块名；在执行文件中就是指__main__

# 正则表达式
re

# 面向对象
- 类
- 对象
```python
class 类名():
    pass

class Person():
    name = 'zhangsan'
    age = 19
    money = 10000000
    def GetMoney():
        return money
    def GetInfo():
        print('%s-%s\n'%(name, age))
```
- 类变量
- 实例变量
- 定义在__init__内部的变量是实例变量
- 类方法
- 实例方法
- 静态方法