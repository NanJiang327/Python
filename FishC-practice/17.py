def power(x, y):
    return x**y


def euclidean(x, y):
    while y:
        t = x % y
        x = y
        y = t
    return x


def dec2bin(dec):
    temp = []
    result = ''

    while dec:
        quo = dec % 2
        dec = dec // 2
        temp.append(quo)

    while temp:
        result += str(temp.pop())

    return result


print(power(2,3))
print(euclidean(10, 15))
print(dec2bin(10))
