# 完全数
import time
import math

start = time.clock()
for num in range(1, 10000):
    sum = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            sum += factor
            if factor > 1 and num / factor != factor:
                sum += num / factor
    if sum == num:
        print(num)
end = time.clock()
print("执行时间:", (end - start), "秒")