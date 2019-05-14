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
    print('called ')

    def __init__(self, name):
        self.__name = name
        Test.count += 1


t1 = Test('Aaron')
print(t1.count)

t2 = Test('Aaron2')
print(t2.count)
