# -*- coding: utf-8 -*-

# 新建一个类
'''
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score        

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


lisa = Student('Lisa', 98)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())
'''

# 把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
'''
class Student(object):
    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender
    
    def set_gender(self,gender):
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
             raise ValueError('error gender')

    def get_gender(self):
        return self.__gender

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

'''
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
'''
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

'''
# 实现一个Fib类用作可以 for ... in 循环
'''
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)
'''
from enum import Enum

Month = Enum('Month1', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name,'=>',member,',',member.value)