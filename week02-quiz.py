# 2주차 퀴즈

# 문제 1
class Foo:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print('I am' + self.name)

class Bar(Foo):
    def __init__(self, name):
        self.name = name
    def speak(self):
        print('You are ' + self.name)

bar = Bar('John')
bar.speak()
# 문제 6
# def int_sum(*args):
#     try:
#         for n in args:
#             sum += n
#     except:
#         print('error')
#     return(sum)
# int_sum('a', 'b')
# int_sum(1)


# 문제 7
from pkg.calculations import add
print(add(1, 2))

# 문제 8
import datetime
now = datetime.datetime.now()
print(now)

import copy

a = [1,2]
b = copy.deepcopy(a)
c = a
print(id(a))
print(id(b))
print(id(c))