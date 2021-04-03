# Section08
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# .  : 현재 디렉토리

# 사용1(클래스)


from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex1 : ", Fibonacci.fib2(400))
print("ex1 : ", Fibonacci().title)



# 사용2(클래스) !!권장하지 않음!!
from pkg.fibonacci import *
# 사용하지도 않는 패키지를 가져오는 것은 리소스 낭비

# 사용3(클래스)

from pkg.fibonacci import Fibonacci as fb

fb.fib(1000)

print("ex3 : ", fb.fib2(1600))
print("ex3 : ", fb().title)


# 사용4(함수)
import pkg.calculations as c

print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))

# 사용5(함수)
from pkg.calculations import div as d
# 필요한 만큼만, 함수를 하나만 가져오는 방법
print("ex5 : ", int(d(100, 10)))

# 사용6
import pkg.prints as p
import builtins
# 기본적으로 불러오는 패키지들
p.prt1()
p.prt2()
print(dir(builtins))






