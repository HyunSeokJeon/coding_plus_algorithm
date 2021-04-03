def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

hi_func = outer_function('Hi')
bye_func = outer_function('Bye')

hi_func()
bye_func()

# 데코레이터 코드
def decorator_function(original_function):  #1
    def wrapper_function():                 #5
        return original_function()          #7
    return wrapper_function                 #6

def display():                              #2
    print('display 함수가 실행됐습니다.')   #8

decorated_display = decorator_function(display)#3
decorated_display()                         #4

# 복잡한 순서를 가지고 있지만
# 기존의 코드를 수정하지 않고도 래퍼 함수를 사용하여 여러 기능을 추가할 수 있다
