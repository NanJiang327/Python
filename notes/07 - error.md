# Try catch finally
```Python
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

# 还可以加个else语句
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
# 当没有错误发生时，会自动执行else语句
else:
    print('no error!')
finally:
    print('finally...')
print('END')
```
# Logging
```Python
import logging
# 可以设置不同级别debug, info, warning, error
# 记录信息级别为info
logging.basicConfig(level=logging.INFO)

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')


s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

# 输出
ZeroDivisionError
```
# Raise error
```Python
# err_reraise.py

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
```
# assert
```Python
def foo(s):
    n = int(s)
    # 表达式n != 0应该是True, 否则代码出错
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
```
# Unit test
```Python
# mydict_test.py

import unittest

from mydict import Dict

class TestDict(unittest.TestCase):
    # 测试方法名字必须以test开头
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
            
    # 测试开始前执行的方法        
    def setUp(self):
        print('setUp...')

    # 测试结束后执行的方法
    def tearDown(self):
        print('tearDown...')
            
# 运行单元测试
# 最简单的运行方式是在mydict_test.py的最后加上两行代码：
if __name__ == '__main__':
    unittest.main()
    
# 运行
python -m unittest mydict_test
```