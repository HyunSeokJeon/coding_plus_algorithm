# closure1.py 에서 계속되는 파일

# closure가 변수값을 저장하는 비밀
def outer_func():  #1
    message = 'Hi'  #3

    def inner_func():  #4
        print(message)  #6

    return inner_func  #5

my_func = outer_func()  #2
print(my_func)
print()
print(dir(my_func))
print()
print(type(my_func.__closure__))
print()
print(my_func.__closure__)
print()
print(my_func.__closure__[0])
print()
print(dir(my_func.__closure__[0]))
print()
print(my_func.__closure__[0].cell_contents)

# 함수의 파라메터를 사용하여 closure 응용
def outer_func(tag):
    text = 'Some text'
    tag = tag
    def inner_func():
        print('<{0}>{1}<{0}>'.format(tag, text))
    
    return inner_func

h1_func = outer_func('h1')
p_func = outer_func('p')

h1_func()
p_func()

# 함수의 파라메터로 HTML 태그를 컨트롤 하는 함수가 만들어짐

# 태그안의 문자열을 컨트롤하는 함수

def outer_func1(tag):
    tag = tag

    def inner_func1(txt):
        text = txt
        print('<{0}>{1}<{0}>'.format(tag, txt))

    return inner_func1

h1_func1 = outer_func1('h1')
p_func1 = outer_func1('p')

h1_func1('h1태그의 내용')
p_func1('p태그의 내용')



