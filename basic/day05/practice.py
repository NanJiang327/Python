

def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num



def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False


# if __name__ == '__main__':
#     num = int(input('请输入正整数: '))
#     if is_palindrome(num) and is_prime(num):
#         print('%d是回文素数' % num)

a = ['a','a','b','a','b','c']
b = {}
for x in a:
    if not b.get(x):
        b[x] = 1
    else:
        b[x] = b[x] + 1

print(b)


def person(name, age, city='beijing'):
    print(name, age, city)


person('Nan', 20)


def person1(name, age, *, city, **kw):
    print(name, age, city, kw)


person1('Nan2', 21, city='gz')


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        print('--break0--', n)
        move(n-1, a, c, b) # move(2, a, c, b) -> move(1, a, b, c)
        print('--break1--', n)
        move(1, a, b, c)
        print('--break2--', n)
        move(n-1, b, a, c)


move(3, 'A', 'B', 'C')


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2015-3-25')


print(now.__name__)


def _iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

def build(x, y):
    return lambda: x * x + y * y


aBuild = build(2, 3)


print(aBuild())