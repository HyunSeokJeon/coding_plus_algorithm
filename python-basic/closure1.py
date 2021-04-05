# python closure

# closure
def outer_func(): #1
    message = 'hi' #3

    def inner_func(): #4
        print(message) #6
    
    return inner_func() #5

outer_func() #2
# hi 출력

# closure2
def outer_func2(): #1
    message = 'hi' #3

    def inner_func2(): #4
        print(message) #6
    
    return inner_func2 #5

outer_func2() #2
# 출력내용 없음
# inner_func2 함수를 실행하는게 아니라 함수 오브젝트를 리턴했기 때문
    
# closure3
def outer_func3(): #1
    message = 'hi' #3

    def inner_func3(): #4
        print(message) #6
    
    return inner_func3 #5

my_func = outer_func3() #2
# 이것도 출력내용 없음
# 함수 오브젝트를 리턴했다면 my_func에 inner_func3 가 할당되었는지 확인
print(my_func)
# <function outer_func3.<locals>.inner_func3 at 0x0000020B7A45CA60>
# inner_func3 함수가 할당되어 있음

my_func() #7
my_func() #8
my_func() #9
# Hi
# Hi
# Hi

# outer_func3는 #2에서 호출된 후 종료되었음
# 그런데 호출된 my_func 함수가 outer_func3함수의 로컬변수인 message를 참조했다.

# closure.py에서 계속..



