# 文件读写
```Python
# 读文件

f = open('/User/NAN/test.txt', 'r') # r表示读

# 如果文件存在
f.read() # 读取文件全部内容
f.close() # 关闭文件

# 避免IOError
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()
        
# 使用with避免每次都写f.close
with open('/path/to/file', 'r') as f:
    print(f.read())
    
# 读取size个字节的内容
f.read(size)
# 读取所有内容并按行返回
for line in f.readlines():
    print(line.strip())
    
# 二进制文件 - 使用rb模式
f = open('/Users/michael/test.jpg', 'rb')
f.read() # b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...'

# 读取非utf-8编码的文件
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
# 读取编码不规范的文件, 设置errors=ignore来忽略错误
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')


# 写文件
# 标识符w 或者 wb 表示写文件或者写二进制文件(会覆盖)
# 使用a标识符表示追加
f = open('/Users/michael/test.txt', 'w')
f.write('Hello, world')
f.close()
# 你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。
# 当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。
# 只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
# 忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')
```
# StringIO 和 BytesIO
```Python
# StringIO

# StringIO 是在内存中读写str
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
# getvalue() 获取写入后的str
print(f.getvalue()) # hello world!

# 或者
 from io import StringIO
 f = StringIO('Hello!\nHi!\nGoodbye!')
 while True:
     s = f.readline()
     if s == '':        
     break
     print(s.strip())

Hello!
Hi!
Goodbye!

# BytesIO
# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue()) # b'\xe4\xb8\xad\xe6\x96\x87'

# 或者
from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read() # b'\xe4\xb8\xad\xe6\x96\x87'

```
# 操作文件
```Python
import os
os.name # 操作系统名
os.environ # 环境变量

# 绝对路径
os.path.abspath('.')
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('/Users/NAN', 'testdir')
# 创建一个目录
os.mkdir('/Users/michael/testdir')
# 删除一个目录
os.rmdir('/Users/michael/testdir')
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
#这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
part-1/part-2
# 而Windows下会返回这样的字符串：
part-1\part-2
# 拆分最后级别的目录或文件名
os.path.split('/Users/michael/testdir/file.txt') # ('/Users/michael/testdir', 'file.txt')
# 获取文件扩展名
os.path.splitext() # ('/path/to/file', '.txt')
# 重命名文件
os.rename('test.txt', 'test.py')
# 删除文件
os.remove('test.py')
# 过滤文件
[x for x in os.listdir('.') if os.path.isdir(x)]
# 获取所有.py文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
```
# 序列化
```Python
# pickle
import pickle
d = dict(name='Bob', age=20, score=88)
# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# 读取
f = open('dump.txt', 'rb')
# 反序列化
d = pickle.load(f)
f.close()
d # {'age': 20, 'score': 88, 'name': 'Bob'}

# json
json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)

import json

d = dict(name='Bob', age=20, score=88)
# 序列化
json.dumps(d) # '{"age": 20, "score": 88, "name": "Bob"}'
# 反序列化
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str) # {'age': 20, 'score': 88, 'name': 'Bob'}

# json 进阶
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s)) # TYPEERROR!

# 前面的代码之所以无法把Student类实例序列化为JSON
# 是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象
# 写一个转换函数
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
# Student实例首先被student2dict()函数转换成dict
print(json.dumps(s, default=student2dict))
# 使用__dict__, 把任意class的实例变为dict
print(json.dumps(s, default=lambda obj: obj.__dict__))

# 反序列化
# 如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
    
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# 反序列化
print(json.loads(json_str, object_hook=dict2student))