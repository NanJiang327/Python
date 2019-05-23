# 0
dict1 = {'F': 70, 'C': 67, 'h': 104, 'i': 105, 's': 115}
dict2 = dict((('F', 70), ('i', 105)))
print(dict1['C'])

# 1
data = '1000,nan,male'
data.split(',')

# 2
dict3 = {}
while True:
    print('--------------------------')
    print('欢迎进入通讯录系统\n1:查询联系人资料\n2:插入新的联系人\n3:删除已有联系人\n4:退出通讯录系统')
    useri = input('请输入相关的指令代码: ')

    if not useri.isdigit() or int(useri) < 1 or int(useri) > 5:
        raise ValueError('请输入正确数字')
    elif int(useri) == 1:
        if len(dict3) == 0:
            print('没有用户')
        else:
            for x, v in dict3.items():
                print('用户', x, '的电话是:', v)
    elif int(useri) == 2:
        username = input('请输入联系人名字: ')
        number = input("请输入用户联系电话: ")
        if dict3.get(username):
            print('您输入的姓名在通讯录中已存在 -->>', username, ':', dict3[username])
            change = input('是否修改用户资料(YES/NO)').lower()
            while change != 'yes' or change != 'no':
                change = input('请输入yes或no').lower()
                if change == 'yes':
                    dict3[username] = number
                    username = None
                    number = None
                else:
                    pass
        else:
            dict3[username] = number
            username = None
            number = None
    elif int(useri) == 3:
        username = input('请输入联系人名字: ')
        if dict3.get(username):
            dict3.pop(username)
            print('用户', username, '已经删除')
        else:
            print('用户不存在')
    elif int(useri) == 4:
        exit('|--- 感谢使用通讯录系统 ---|')
