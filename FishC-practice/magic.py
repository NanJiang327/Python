import time
from threading import Thread

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height  = height

    def __setattr__(self, name, value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            # super().__setattr__(name, value)
            # or
            self.__dict__[name] = value

    def getArea(self):
        return self.width * self.height


r1 = Rectangle(4,5)


class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance, value)

    def __delete__(self, instance):
        self.fdel(instance)


class C:
    def __init__(self):
        self._x = None

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def delX(self):
        del self._x

    x = MyProperty(getX, setX, delX)


class MyThread(Thread):
    def __init__(self, name='Python'):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(2):
            print("Hello", self.name)
            time.sleep(1)


if __name__ == '__main__':
    # 创建线程01，不指定参数
    thread_01 = MyThread()
    # 创建线程02，指定参数
    thread_02 = MyThread("MING")

    thread_01.start()
    thread_02.start()