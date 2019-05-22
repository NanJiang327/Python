' a test module '

__author__ = 'Aaron Jiang'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello World')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('TOO MANY ARGUMENTS!')


if __name__ == '__main__':
    test()


class Test():
    count = 0
    print('called ', count)

    def __init__(self, name):
        self.__name = name
        Test.count += 1


t1 = Test('Aaron')
print(t1.count)

Test.count = 10

t2 = Test('Aaron2')
print(t2.count)


class Screen:
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def resolution(self):
        return self._width * self.__height


sc = Screen()
sc.width = 1024
sc.height = 1
print(sc.resolution)

class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain('/nan').status.user.timeline.list)
