# Class
```Python
class Student():
    def __init__(self, name, score, distance):
        self.name = name
        self.score = score
        # 私有变量 __xx
        self.__distance = distance
        
    def print_score(self):
        print('%s: %s' % (self.name, self.score))
        
    def get_distance(self):
        return self.__distance
        
    def set_distance(self, distance):
         if 0 <= distance <= 100:
            self.__distance = distance
        else:
            raise ValueError('bad distance')
            
            
# 依旧可以访问private
s = Student('Aar', 12, 15)
s._Student__distance # 15
```
# 继承
```Python
class Fish:
    def __init__(self):
        self.x = 10
        self.y = 10
        
    def move(self):
        self.x -= 1
        print('my position is', self.x)
        

class Shark(Fish):
    def __init__(self):
        # 调用父类初始方法
        super().__init__()
        self.hungry = True
        
    def eat(self):
        print('Eat!')
        
```
# 判断类型
```Python
a = Animal()
d = Dog()
h = Husky()

isinstance(h, Husky) # True
isinstance(h, Dog) # True
isinstance(h, Animal) # True
isinstance(d, Dog) and isinstance(d, Animal) # True


isinstance('a', str) # True
isinstance(123, int) # True
isinstance(b'a', bytes) # True

# 判断是否是某些类型中的一种
isinstance([1, 2, 3], (list, tuple)) # True
isinstance((1, 2, 3), (list, tuple)) # True
```
# 内置方法 getattr(), setattr(), hasattr()
```Python
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
        
obj = MyObject()

# 有属性'x'吗？
hasattr(obj, 'x') # True

# 有属性'y'吗？
hasattr(obj, 'y') # False

# 设置一个属性'y'
setattr(obj, 'y', 19) 
# 有属性'y'吗？
hasattr(obj, 'y') # True
# 获取属性'y'
getattr(obj, 'y') #19
# 如果试图获取不存在的属性，会抛出AttributeError的错误：
getattr(obj, 'z') # 获取属性'z'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'MyObject' object has no attribute 'z'
# 获取属性'z'，如果不存在，返回默认值404
getattr(obj, 'z', 404) # 404
```
# 实例属性和类属性
```
class Student(object):
    # 类属性
    name = 'Student'
    def __init__(self, name):
        self.name = name

s = Student('Bob')
# 实例属性
s.score = 90
s.name # Student
# 千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属
# 但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
```

# 描述符
其实也很简单，一个实现了 描述符协议 的类就是一个描述符。

什么描述符协议：实现了  __get__()、__set__()、__delete__() 其中至少一个方法的类，就是一个描述符。
```
__get__： 用于访问属性。它返回属性的值，若属性不存在、不合法等都可以抛出对应的异常。
__set__：将在属性分配操作中调用。不会返回任何内容。
__delete__：控制删除操作。不会返回内容。
```

## 使用原因
```
# 定义一个学生类
class Student:
    def __init__(self, name, math, chinese, english):
        self.name = name
        self.math = math
        self.chinese = chinese
        self.english = english

    @property
    def math(self):
        return self._math

    @math.setter
    def math(self, value):
        if 0 <= value <= 100:
            self._math = value
        else:
            raise ValueError("Valid value must be in [0, 100]")

    @property
    def chinese(self):
        return self._chinese

    @chinese.setter
    def chinese(self, value):
        if 0 <= value <= 100:
            self._chinese = value
        else:
            raise ValueError("Valid value must be in [0, 100]")

    @property
    def english(self):
        return self._english

    @english.setter
    def english(self, value):
        if 0 <= value <= 100:
            self._english = value
        else:
            raise ValueError("Valid value must be in [0, 100]")

    def __repr__(self):
        return "<Student: {}, math:{}, chinese: {}, english:{}>".format(
                s
```
没想到，人外有天，你的主管看了你的代码后，深深地叹了口气：类里的三个属性，math、chinese、english，都使用了 Property 对属性的合法性进行了有效控制。功能上，没有问题，但就是太啰嗦了，三个变量的合法性逻辑都是一样的，只要大于0，小于100 就可以，代码重复率太高了，这里三个成绩还好，但假设还有地理、生物、历史、化学等十几门的成绩呢，这代码简直没法忍。去了解一下 Python 的描述符吧。

## 描述符的例子
```python
class Score:
    def __init__(self, default=0):
        self._score = default
    
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Score must be integer')
        if not 0 <= value <= 100:
            raise ValueError('Vaild value must be in [0,100]')
        
        self._score = value
    
    def __get__(self, instance, owner):
        return self._score
        
    def __delete__(self):
        del self._score
        
class Student:
    math = Score(0)
    chinese = Score(0)
    english = Score(0)

    def __init__(self, name, math, chinese, english):
        self.name = name
        self.math = math
        self.chinese = chinese
        self.english = english


    def __repr__(self):
        return "<Student: {}, math:{}, chinese: {}, english:{}>".format(
                self.name, self.math, self.chinese, self.english
            )
```
## 描述符的访问规则
描述符分两种:
- 数据描述符: 实现了get和set两种方法的描述符
- 非数据描述符: 只实现了get一种方法的描述符

==数据描述器和非数据描述器的区别在于：它们相对于实例的字典的优先级不同。==

如果实例字典中有与描述器同名的属性，如果描述器是数据描述器，优先使用数据描述器，如果是非数据描述器，优先使用字典中的属性。
```python
# 数据描述符
class DataDes:
    def __init__(self, default=0):
        self._score = default

    def __set__(self, instance, value):
        self._score = value

    def __get__(self, instance, owner):
        print("访问数据描述符里的 __get__")
        return self._score

# 非数据描述符
class NoDataDes:
    def __init__(self, default=0):
        self._score = default

    def __get__(self, instance, owner):
        print("访问非数据描述符里的 __get__")
        return self._score


class Student:
    math = DataDes(0)
    chinese = NoDataDes(0)

    def __init__(self, name, math, chinese):
        self.name = name
        self.math = math
        self.chinese = chinese

    def __getattribute__(self, item):
        print("调用 __getattribute__")
        return super(Student, self).__getattribute__(item)

    def __repr__(self):
        return "<Student: {}, math:{}, chinese: {},>".format(
                self.name, self.math, self.chinese)
```
需要注意的是，math 是数据描述符，而 chinese 是非数据描述符。从下面的验证中，可以看出，当实例属性和数据描述符同名时，会优先访问数据描述符（如下面的math），而当实例属性和非数据描述符同名时，会优先访问实例属性（__getattribute__）