from collections import deque
import hashlib, hmac
import itertools

q = deque(['A','B','C'])

q.append('x')
q.appendleft('y')
print(q)

q.pop()
q.popleft()
print(q)

message = 'Hello, world!'
key = 'secret'
h = hmac.new(key.encode('utf-8'), message.encode('utf-8'), digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest())


md5 = hashlib.md5()
md5.update(message.encode('utf-8') + key.encode('utf-8'))
print(md5.hexdigest())

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, ':', list(group))

odd = itertools.count(1, 2)
newn = itertools.takewhile(lambda x: x <=  100, odd)
for n in newn:
    print(n)
