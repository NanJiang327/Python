# 1
nums = 10


def num():
    global nums
    nums = 20
    print(nums)


num()

# 2


def num2():
    x = 5

    def func():
        nonlocal x
        x *= 5
        return x
    return func()


# 3

# 无法访问函数内

# 为什么代码A没报错, 而B报错了
'''
def outside():
    var = 5
    def inside():
        var = 3
        print(var)
        
    inside()
    
outside()


def outside():
    var  = 5
    def inside():
        print(var)
        var = 3
    
    inside()
outside()
'''

# 4
dictionary = {

}


def checkchar(str):
    for x in str:
        print(x)
        if x in dictionary:
            dictionary[x] = dictionary[x] + 1
        else:
            dictionary[x] = 1


list1 = []
str1 = 'asdasdasjbdwqueqw,onvnqdpasldqbnjwd'

for each in str1:
    if each not in list1:
        if each == '\n':
            print('\\n', str1.count(each))
        else:
            print(each, str1.count(each))
    list1.append(each)

checkchar('abcdsad9ijqiwenqjdasldj qwebudsjwqe')
print(dictionary)


# 5
str1 = 'asdasdasjbdwqueqw,onvnqdpasldqbnjwd'
countA = 0
countB = 0
countC = 0
length = len(str1)
for i in range(length):
    if str1[i] == '\n':
        continue
    if str[i].isupper():
        if countB == 1:
            countC += 1
            countA = 0
        else:
            countA += 1
        continue
    if str1[i].islower() and countA == 3:
        countB = 1
        countA = 0
        target = 1
        continue
    if str1[i].islower() and countC == 3:
        print(str1[target], end='')

    countA = 0
    countB = 0
    countC = 0