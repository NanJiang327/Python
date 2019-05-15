# slice
```Python
L = ['A','B','C','D']
# take 3 elements
L[0:3] or L[:3] # ['A','B','C']
# 倒数切片
L[-2:-1] # ['C','D']
# 每5个取一个
L = list(range(100))
L[::5]
# 复制list
L2 = L[:]
# tuple 切片的结果还是tuple
(0,1,2,3,4)[:3] # (0,1,2)
```
# iteration
```Python
# dictionary iteration
for key in d:
    print(key)

for value in d.values:
    print(value)
    
for key, values in d.items():
    print(key, ':', value)


# 判断是否可迭代
from collections import Iterable
isinstance('abc', Iterable) # True
isinstance([1,2,3], Iterable) # True
isinstance(123, Iterable) # False

# 实现循环下标
for i, value in enumerate(['A','B','C']):
    print(i, value)
    
# 0 A, 1 B, 2 C

# 两个变量循环
for x, y in [(1, 1),(2, 4),(3, 9)]
    print (x, y) # 1 1, 2 4, 3 9
```
# list comprehensions
```Python
# 生成x^2 的list
[x * x for x in range(1,11)]
# 偶数平方list
[x * x for x in range(1,11) if x % 2 == 0]
# 双层循环
[m + n for m in 'ABC' for n in 'XYZ']
# 生成目录下所有文件和目录名
import ox
[d for d in os.listdir('.')]
# ['.emacs.d', '.ssh', '.Trash', 'Adlm', 'Applications', 'Desktop', 'Documents', 'Downloads', 'Library', 'Movies', 'Music', 'Pictures', 'Public', 'VirtualBox VMs', 'Workspace', 'XCode']
# 把list 中所有的字符串变小写
[s.lower() for s in L] # ['hello', 'world', 'ibm', 'apple']
# 两个变量生成list
[k + '=' + v for k, v in d.items()]
# ['y=B', 'x=A', 'z=C']
```
# generator
```Python
g = (x * x for x in range(10))
# next()
next(g) # 0
next(g) # 1
...
next(g) # 64
next(g) # 81

# 迭代generator
for n in g:
    print(n)
    
a, b = b, a + b
# 相当于
t = (b, a + b) # t 是tuple
a = t[0]
b = t[0]

# 定义generator的另一种方法 - 函数定义中包含yield关键字
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return done
    
# 获取generator的return语句
while True:
     try:
         x = next(g)
         print('g:', x)
     except StopIteration as e:
         print('Generator return value:', e.value)
         break
```