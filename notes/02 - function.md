# bif
```
abs() # 绝对值
int() # 转整数
str() # 转字符串
float() # 转浮点
bool() # 转boolean
hex() # 转十六进制
max(1, 3, 5, 7) # 7 - 求最大值
min(1, 3, 5) # 1 -求最小值
```
# funtion
```
# 返回多值 - 本质上是返回tuple
def some():
    return 1, 2 # tuple (1, 2)
    
# position argument
def power(x):
    pass
    
    
# default argument
def power(x, y=5):
    pass
    
power(2)
power(2, 3)

# Arbitrary argument
def calc(*nums):
    sum = 9
    for n in nums:
        sum += n
    return sum
    
calc(1, 2)
numslist = [1, 2, 3]
calc(*numslist)

# keyword argument
def person(name, age, **keyword):
    print(keyword)
    
person('A', 23, city='beijing', job='developer') # {'city' = 'beijing', 'job' = 'developer'}

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job']) # {'city': 'Beijing', 'job': 'Engineer'}

# 命名关键字参数
def person(name, age, *, city, job) # 只接受city和job作为关键字
```

# 递归
```
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

===> 5 * (4 * (3 * (2 * fact(1))))
===> 120

# 尾递归 - 无论调用多少次 都只占一个栈帧
# return 语句不能包含表达式
def fact(n):
    return fact_iter(n, 1)
    
def fact_iter(num, result):
    if num == 1:
        retun result
    return fact_iter(num - 1, num * result)
    
===> fact_iter(5, 1)
===> fact_iter(4, 5)
===> fact_iter(3, 20)
===> fact_iter(2, 60)
===> fact_iter(1, 120)
===> 120
```