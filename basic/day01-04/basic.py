import random

# For loop

sum = 0
for x in range(1, 101):
  if x % 2 == 0:
    sum += x
print(sum)

import random


# While loop
answer = random.randint(1, 100)
counter = 0
while False:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')


row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()