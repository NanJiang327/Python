# 水仙花数
for num in range(100, 10000):
    low = num % 100
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)