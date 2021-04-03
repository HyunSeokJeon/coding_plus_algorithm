# Section05-2
# 파이썬 흐름제어(반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 : for, while

v1 = 1
while v1 < 11:
    print('v1 is :', v1)
    v1 += 1

for v2 in range(10):
    print('v2 is : ', v2)

for v3 in range(1, 10):
    print('v3 is :', v3)

# 1 ~ 100 합

sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1 ~ 100 : ', sum1)
print('1 ~ 100 : ', sum(range(1, 101)))

print('1 ~ 100 : ', sum(range(1, 100, 2)))

# 시쿼스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전

# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip
names = ['Kim', 'Park', 'Cho', 'Choi', 'Ioo']

for name in names:
    print('You are : ', name)

word = 'dreams'

for s in word:
    print('word : ', s)

my_info = {
    'name': 'Kim',
    'age': 33,
    'city': 'Seoul'
}
# dict 반복문으로 출력하기 (기본값 : keys)
# 값
for key in my_info.values():
    print('my_info', key)
# 키
for key in my_info.keys():
    print('my_info', key)
# 키 & 값
for key in my_info.items():
    print('my_info', key)

name = 'KennRY'

for n in name:
    if(n.isupper):
        print(n.lower())
    else:
        print(n.upper())

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 37, 15, 34, 36, 18]

for num in numbers:
    if num == 33:
        print('found : 33!')
        break
    else:
        print('not found : 33!')

# for-else 구문 (반복문이 정상적으로 수해 된 경우 else 블럭 수행)
for num in numbers:
    if num == 33:
        print('found : 33!')
        break
    else:
        print('not found : 33!')
# break를 만나면 else가 수행이 안됨
else:
    print('not found : 33....')


# continue

lt = ['1', 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) == float:
        continue
    print('타입: ', type(v))

name = 'Niceman'
print(list(reversed(name)))
print(tuple(reversed(name)))





