from random import randint


def factorial(num):
    """
    求阶乘

    :param num: 非负整数
    :return: num的阶乘
    """
    result = 1
    for x in range(1, num + 1):
        result *= x
    return result


m = int(input('m = '))
n = int(input('n = '))

print(factorial(m) // factorial(n) // factorial(n - m))


def roll_dice(y=2):
    total = 0
    for _ in range(y):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c


# 如果没有指定参数那么使用默认摇两颗色子
print(roll_dice())
# 3颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传参可不按顺序传
print(add(c=50, b=100, a=200))


def add2(*args):
    total = 0
    for val in args:
        total += val
    return total
