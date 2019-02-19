# -*- coding: utf-8 -*-

''' 
#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
def trim(s):
    if s[:1] != ' ' and s[-1:] != ' ' :
        return s
    elif s[:1] == ' ':
        return trim(s[1:])
    else:
        return trim(s[:-1])

print('s =',trim('      hello ')) 
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
'''

'''
#请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
      if L != []:
        (min,max)=(L[0],L[0])
        for x in L:
           if x > max:
             max = x
           if x < min:
             min = x
        return (min,max)
      else:
         return (None, None)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
'''

'''
#请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
L1 = ['Hello', 'World', 18, 'Apple', None]  
L2 = [x.lower() for x in L1 if isinstance(x, str)==1]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
'''


# 把每行看成一个list，试写一个generator，不断输出下一行的list：
'''
def triangles():
    L=[1]
    yield L
    while True:
        L = [1] + [L[x]+L[x+1] for x in range(len(L)-1)]+[1]
        yield L

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('ok')
else:
    print('NG')
'''
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
'''
def normalize(name):
    name=name[0].upper()+name[1:].lower()
    return name

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
'''

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
'''
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(s):
    def fn(x,y):
        print(x,y)
        return x * 10 + y
    def char2mun(s):
        return DIGITS[s]
    n = s.index('.')
    s1 = list(map(int,[x for x in s[:n]]))
    s2 = list(map(int,[x for x in s[n+1:]]))
    return reduce(fn,s1)+reduce(fn,s2)/10**len(s2)

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
'''

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
'''
# 方案一
def is_palindrome(n):
    l = str(n)
    for k in range(0,len(l)):
        if l[k] != l[-k-1]:
            return False
    return True 
# 方案二
def is_palindrome(n):
    nn = str(n) #转成字符串
    return nn == nn[::-1] #反转字符串并对比原字符串返回true/false
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
'''
# 利用闭包返回一个计数器函数，每次调用它返回递增整数
'''
def createCounter():
    def creat_counter():
        c = 1
        while True:
            yield c
            c += 1
    cc = creat_counter()
    def counter():
        return next(cc)
    return counter

# 测试
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5

counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
'''

# 编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
# 使其既支持：@log 又支持：@log('execute')
'''
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call')
            print("%s func = %s" % (text, func.__name__))
            r = func(*args, **kw)
            print('end call')
            return r
        return wrapper
    return decorator if isinstance(text, str) else decorator(text)

# 测试
@log
def f():
    pass
f()

@log('execute')
def g():
    pass
g()
'''

