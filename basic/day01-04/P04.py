# 斐波那契数列
a = 0
b = 1
for num in range(20):
    (a, b) = (b, a+b)
    print(a, end=' ')
