def same(str1):
    return True if str1 == str1[::-1] else False


def count(*params):
    length = len(params)
    for i in range(length):
        letters = 0
        space = 0
        digit = 0
        others = 0
        for each in params[i]:
            if each.isalpha():
                letters += 1
            elif each.isdigit():
                digit += 1
            elif each == ' ':
                space += 1
            else:
                others += 1
        print('第 %d 个字符串共有: 英文字母 %d 个, 数字 %d 个, 空格 %d 个, 其他字符 %d 个.' % (i+1, letters, digit, space, others))


print(same('sadas'))
count('I love fishc.com.', 'I love you, you love me')
