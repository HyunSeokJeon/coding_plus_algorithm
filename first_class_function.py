# 퍼스트클래스 함수
# 프로그래밍 언어가 함수를 first-class citizen으로 취급하게 만들어준다

def square(x):
    return x * x

print(square(5))

f = square

print(square)
print(f)

# 간단한 함수를 정의 그리고 호출
# square 함수를 f 라는 변수에 할당
# <function square at 0x000001CE875DCB80>
# <function square at 0x000001CE875DCB80>
# 메모리 주소값이 같은 square 함수 오브젝트가 할당되어 있는 것을 확인

# f도 진짜 함수처럼 호출할 수 있는지 확인

print(f(5))
# 25

# 프로그래밍 언어가 퍼스트클래스 함수를 지원하면 변수에 함수를 할당할 수 있고
# 인자로써 다른함수에 전달하거나, 함수의 리턴값으로도 사용 할 수가 있다

def my_map(func, arg_list: list) -> list:
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

num_list = [1, 2, 3, 4, 5]

squares = my_map(square, num_list)

print(squares)

# 그냥 square를 식으로 i * i 로 쓰면되지 않나?
# 그렇지만 함수가 여러개라면 재사용할 수가 있다는 장점이 있다
# 위에 square이 선언되어 있으므로 선언생략
def cube(x):
    return x * x * x

def quad(x):
    return x * x * x * x

cubes = my_map(cube, num_list)
quads = my_map(quad, num_list)

print(cubes)
print(quads)
# 여러개의 함수나 모듈이 있을 경우 my_map같은 warpper 함수 하나로 재사용이 가능

# 함수의 결과값으로 또 다른 함수를 리턴하는 방법(클로저)
def logger(msg):

    def log_message():
        print('Log: ', msg)

    return log_message

log_hi = logger('Hi')

print(log_hi)
# log_message 오브젝트 출력
log_hi()

del logger

try:
    print(logger)
except NameError:
    print('NameError: logger는 존재하지 않습니다.')

log_hi()

# log_hi 내부에 __closure__에 함수 내용을 저장하고 있어서 가능
print(log_hi)

print(dir(log_hi))

print(log_hi.__closure__)

print(log_hi.__closure__[0])

print(dir(log_hi.__closure__[0]))

print(log_hi.__closure__[0].cell_contents)