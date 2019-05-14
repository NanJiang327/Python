# 字符串编码
```Python
# bytes类型的数据
x = b'ABC'

'ABC'.encode('ascii') # b'ABC'
'中文'.encode('utf-8') # b'\xe4\xb8\xad\xe6\x96\x87'
b'ABC'.decode('ascii')

# 整数 | 浮点数 | 字符串 | 十六进制数
%d | %f | %s | %x

# 整数和浮点数指定位数和补0
%02d, 1 # 01
$.2f, 3.1415926 # 3.14
```

# list 和 tuple
list
```Python
# --- list ----
classmates = ['A','B','C']
# length
len(classmates)
# 序列
classmates[0] # A
# 倒序
classmates[-1] # C
# 添加
classmates.append('D')
# 添加指定位置
classmates.insert(1, 'BB')
# 删除最后
classmates.pop()
# 删除指定位置
classmates.pop(1)
# 替换
classmates[0] = 'rA'
# 查找
classmates.find('A') # 0 找不到会返回-1
classmates.index('A') # 0 找不到会异常
```
tuple
```Python
tuplel = ('A', 'B', 'C')
# tuple 不可变
# 空 tuple
tuple1 = ()
# 一个元素的tuple
tuple1 = (1,)
```

# range 和 list
```Python
# 生成0 - 99 数
range(100)
# 使用list转换
list(range(100)) # [0, 1, 2, ...,97, 98, 99]
```

# while
```Python
while True:
    if condition:
        break # 结束当前循环
    else:
        continue # 下轮循环
        # continue 后的语句不执行
        print('say') # 不执行
```

# dict and set
```Python
# dict
dict1 = {'Aaron': 100, 'Yi': 86, 'Gu': 72}
dict1['Aaron'] # 100

# 一个key只能对应一个value
dict['Aaron'] = 101 # Aaron值为101

# key exist?
'Aaron' in dict1 # True
dict1.get('Thomas') # None
# 指定不存在返回的value
dict1.get('Thomas', -1) # -1

# 删除一个key
dict1.pop('Yi')

# key 必须为不可变对象
key = [1, 2, 3]
dict1[key] = 'a list' # Error!

# copy dict
dict2 = dict1.copy()
```
set
```Python
s = set([1, 2, 3])
s2 = {2, 3, 4, 5, 6}

# add key
s.add(4)
# remove key
s.remove(1)

# 交集 并集
s & s2 # {2, 3}
s3 = s | s2 # {1, 2, 3, 4, 5, 6}

# 移除
newS = s3 - s2 # {1}
```
