# 0
lambda x, y = 3 : x * y

# 3
threelist = list(filter(lambda n: not(n%3), range(1, 100)))
print(threelist)

# 1 2  4 5
def fun_b(x):
    return x if x % 2 else None


def odd(x):
    return x % 2


nums = range(1, 11)

new = filter(odd, nums)

print(list(new))

even = filter(lambda x: x % 2, nums)

print(list(even))

odd = filter(lambda x: x % 2 == 0, nums)

print(list(odd))

newl = list(map(lambda x, y: [x, y], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))

print(newl)



# 6
# 16 和 FishCFishC