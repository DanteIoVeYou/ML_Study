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

# 模块与包
- 解释器内建模块
- python标准库
- 第三方模块
- 应用程序自定义模块
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