# 여러 기능을 추가하는 데코레이션 함수
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('{} 함수가 호출되기 전입니다.'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display_1():
    print('display_1 함수가 실행됐습니다.')

@decorator_function
def display_2():
    print('display_2 함수가 실행됐습니다.')

# display_1 = decorator_function(display_1)
# display_2 = decorator_function(display_2)

display_1()
print()
display_2()

@decorator_function
def display():
    print('display 함수가 실행됐습니다')

@decorator_function
def display_info(name, age):
    print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))

display()
print()
display_info('John', 25)

class DecoratorClass:
    def __init__(self, original_function):
        self.original_function = original_function
    
    def __call__(self, *args, **kwargs):
        print('{} 함수가 호출되기 전입니다.'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@DecoratorClass
def displayInClass():
    print('displayInClass 함수가 실행됐습니다.')

@DecoratorClass
def display_infoInClass(name, age):
    print('display_infoInClass({}, {}) 함수가 실행됐습니다.'.format(name, age))

displayInClass()
print()
display_infoInClass('John', 25)

