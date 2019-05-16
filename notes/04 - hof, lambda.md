# map/reduct, filter sorted
```Python
# map
def f(x):
    return x * x
r = map(f, [1,2,3,4,5,6,7,8,9])
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

# map 返回的结果是iterator 需要用list()函数把整个序列计算出来返回一个lisst
list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

# reduce
from functools import reduce
def add(x, y):
    return x + y
    
reduce(add, [1, 3, 5, 7, 9]) # 25
reduce(lambda x, y: x + y, [1,3,5,7,9]) # 25

# filter
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
list(filter(lambda x: x % 2 == 1, [1, 2, 4, 5, 6, 9, 10, 15])

# sorted
sorted([36, 5, -12, 9, -21]) # [-21, -12, 5, 9, 36]
# 接受参数 - 按绝对值排序
sorted([36, 5, -12, 9, -21], key=abs) # [5, 9, -12, -21, 36]
# 忽略大小写排序
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower) 
# 反向排序
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
['Zoo', 'Credit', 'bob', 'about']
```
# 匿名函数 - lambda
```Python
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8])) # [1, 4, 8, 16, 25, 36, 49, 64, 81]
# 返回匿名函数
def build(x, y):
    return lambda: x * x + y * y
```
# Decorator
```Python
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log # 相当于 now = log(now)
def now():
    print('2015-3-25') # call now(): 2015-3-25
    
# 带参数
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute') # 相当于now = log('excute')(now)
def now():
    print('2015-3-25') # excute now(): 2015-3-25
    
# 更改签名
now.__name__ # wrapper

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
    
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
   
now.__name__ # now    
```
# Partial function
```Python
import functools
# 实际上固定了int()函数的关键字参数base
int2 = functools.partial(int, base=2)
int2('1000000') # 64
# 相当于
kw ={'base': 2}
int('10010', **kw)

# 另外一个例子
max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分添加到左边
max2(2, 5, 6)
# 相当于
args = (10, 2, 5, 6)
max(*args) # 10
```
# 模块
```Python
mycompany # __init__.py 必须存在
├─ __init__.py
├─ abc.py
└─ xyz.py
# 模块名字
mycompany.abc 和 mycompany.xyz

mycompany
 ├─ web
 │  ├─ __init__.py
 │  ├─ utils.py
 │  └─ www.py
 ├─ __init__.py
 ├─ abc.py
 └─ xyz.py
 # 模块名
 mycompany.web.www 和 mycompany.web.utils
 
 # 使用模块
 #!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module ' # 文本注释

__author__ = 'Michael Liao' # 作者变量

import sys # 引入模块

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

# 当我们运行hello模块文件时
# python解释器会把一个特殊变量__name__设置为__main__, 
# 而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
if __name__=='__main__':
    test()
 
 
 # sys模块有一个argv变量，用list存储了命令行的所有参数
 # 运行python3 hello.py获得的sys.argv就是['hello.py']；

# 运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael]。
```
# 作用域
```
1. abc, x123 公开的变量
2. __xx__ 如: __author__, __name__ 特殊变量, 尽量不要使用这种命名
3. _xx 和 __xx 是非公开变量, 不应该直接被引用, 比如_abc, __abc
```
之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。