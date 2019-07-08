def result(*nums, base=3):
    sum = 0
    for x in nums:
        sum += x
    return sum * base


def follower():
    for each in range(100, 1000):
        temp = each
        sums = 0
        while temp:
            sums = sums + (temp % 10) ** 3
            temp = temp // 10
        if sums == each:
            print(each, end='\t')


def strcount():
    count = 0
    print('============ START =================')
    str1 = input('请输入字符串:')
    target = input('请输入目标字符串:')
    targetlength = len(target)
    for x in range(len(str1)):
        if target == str1[x: x + targetlength]:
            count += 1
    print(target, ' 出现了', count, '次')



# print(result(2, 4, 6, 7))
# print('所有水仙花数分别是: ', end='')
# follower()
# strcount()
