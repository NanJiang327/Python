# 动态绑定方法
```Python
# 正常情况下，当我们定义了一个class，创建了一个class的实例后
# 我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。
class Student(object):
    pass
    
s = Student()
s.name = 'Michael'

def set_age(self, age):
    self.age = age

# 给所有实例绑定一个新的方法
Student.set_age = set_age
# 给class绑定方法后, 所有实例都可以调用
s.set_age(12)
s.age # 12
s2.set_age(15)
s2.age # 15
```
# 使用slots 限制实例属性
```Python
class Student(object):
    # 用tuple定义允许绑定的属性名称
    __slots__ = ('name', 'age') 
    
s = Student()
s.name = 'Michael'
s.age = 25
s.score = 99 # Error!

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class GraduateStudent(Stduent):
    pass
    
g = GraduateStudent()
g.score = 9999
```
# @property
```Python
class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
        
        
# 使用property
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
        
    # 不定义setter 就等于设置只读    
    @property
    def age(self):
        return 2015 - self._birth
        
s = Student()
s.score = 70 # 相当于set_score(70)
s.score # 70 相当于get_score
```
# 多继承, MixIn
```Python
class Dog(Mammal, Runnable):
    pass
    
class Bat(Mammal, Flyable):
    pass
```
# 定制类

```Python
# __str__, __repr__, __getattr__
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    # 设置程序开发者看到的字符串
    __repr__ = __str__
    
print(Student('Michael')) # Student object (name: Michael)
# 如果我们调用不存在的属性或者方法时会报错
s.score # Error
# 可以在 Student里添加__getattr__(self, attr)来动态返回属性
class Student(object):
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        # 返回函数    
        if attr=='age':
            return lambda: 25
        # 设置未设置不存在属性的返回值    
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
# 当调用不存在属性时, 会试图调用__getattr__(self, 'score')来尝试获得属性
s.score # 99
s.age # 25
s.abc # Error


# __getitem__, __iter__    
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
    
    # 使用下标取出元素和添加切片方法
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
            

# 对象实例可以调用自身
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('mic')
s() # My name is mic
            
```
# 枚举类
```Python
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
    
@unique # 装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon # Weekday.Mon
Weekday['Tue'] # Weekday.Tue
Weekday.Tue.value # 2
```