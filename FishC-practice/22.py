def times(n):
    sum = 1
    for n in range(1, n):
        sum *= n
    print(sum)


times(5)


def timesrecursion(n):
    if n == 1:
        return 1
    else:
        return n * timesrecursion(n - 1)


timesrecursion(10)


# fab
def feb(num):
    a = 0
    b = 1
    for x in range(num):
        (a, b) = (b, a+b)

    print(a)


feb(12)
# a = 0
# b = 1
# for num in range(20):
#     (a, b) = (b, a+b)
#     print(a, end=' ')


def febrec(num):
    if num == 1 or num == 2:
        return febrec(num - 1) + febrec(num - 2)
    else:
        return 1


print(febrec(12))

