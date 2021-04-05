# Chapter03_1
# 파이썬 심화
# 시퀀스 형 
# 컨테이너 (Container) : 서로 다른 자료형[list, tuple, collections.deque]
# flat : 한 개의 자료형[str, bytes, bytearray, array.array, memoryview]
# 속도차이는 flat이 빠름
# 가변 : list, bytearray, array.array, memoryview, deque
# 불변 : tuple, str, bytes

# 지능형 리스트(Comprehending Lists)

# Non Comprehending Lists
chars = '!@#$%^&*()_+'
codes1 = []

for s in chars:
    codes1.append(ord(s))

# Comprehending Lists
codes2 = [ord(s) for s in chars]  # 대용량 데이터를 다룰때는 빠르다고 한다.

# Comprehending List + Map, Filter
# 속도 약간 우세
codes3 = [ord(s) for s in chars if ord(s) > 40]
codes4 = list(filter(lambda x : x > 40, map(ord, chars)))



print(codes1)
print(codes2)
print(codes3)
print(codes4)
print([chr(s) for s in codes1])
print([chr(s) for s in codes2])
print([chr(s) for s in codes3])
print([chr(s) for s in codes4])

print()
print()

# Generator

import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지x)
tuple_g = (ord(s) for s in chars)

print(tuple_g)
# <generator object <genexpr> at 0x0000023278A77C80>
# 예상 : ( ~~~ ) 근데 generator가 나옴
# 메모리에 올리지 않았다는 것이고 많은 데이터를 다룰 때 성능에 좋다
# 하나씩 받아서 처리할 때는 generator가 유리

print(next(tuple_g))
print(next(tuple_g))


# Array
array_g = array.array('I', (ord(s) for s in chars))

print(array_g)
print(array_g.tolist())

print()
print()
print()

# 제네레이터 예제

print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)):
    print(s)

print()
print()

# 리스트 주의 할 점
marks1 = [['~'] * 3 for n in range(3)]
marks2 = [['~'] * 3 ] * 3  # marks2 객체를 그냥 복사하는 식

print(marks1)
print(marks2)

print()

marks1[0][1] = 'x'
marks2[0][1] = 'x'

print(marks1)
print(marks2)

# 증명
print([id(n) for n in marks1])
print([id(n) for n in marks2])

# Tuple advanced

# Packing & Unpacking

print(divmod(100, 9))
print(divmod(*(100, 9)))
print(*(divmod(100,9)))
# *(  ) unpacking하는 방법이다

x, y, *rest = range(10)
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)
# * ** 의 의미를 다시 생각해볼 수 있는 예제임

print()
print()

# Mutable(가변) vs Immutable(불변)

l = (10, 15, 20)
m = [10, 15, 20]

print(l, m)
print(id(l), id(m))

l = l * 2
m = m * 2

print(l, m, id(l), id(m))  # id 값이 모두 변했다.

l *= 2
m *= 2

print(l, m, id(l), id(m))  # id 값이 튜플은 변했고 list변하지 않고 자기 참조에 재할당

print()
print()

# sort vs sorted
# reverse, key = len, key = str.lower, key = func

f_list = ['orange', 'apple', 'mange', 'papaya', 'lemon', 'strawberry', 'coconut'] 

# sorted : 정렬 후 '새로운' 객체 반환

print(sorted(f_list))
print(sorted(f_list, reverse = True))
print(sorted(f_list, key = len))
print(sorted(f_list, key = lambda x: x[-1])) # 끝글자를 기준으로 정렬
print(sorted(f_list, key = lambda x: x[-1], reverse = True)) # 끝글자를 기준으로 정렬

print(f_list)

print()

# sort : 정렬 후 객체 직접 변경
# 반환 값 확인 None (객체를 직접 변경하구나 라고 어느정도 생각하자)

a = f_list.sort()
print(a, f_list)

print(f_list.sort(), f_list)
print(f_list.sort(reverse = True), f_list)
print(f_list.sort(key = len), f_list)
print(f_list.sort(key = lambda x: x[-1]), f_list)
print(f_list.sort(key = lambda x: x[-1], reverse = True), f_list)





