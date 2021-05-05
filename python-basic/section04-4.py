# Section04-4
# 파이썬 자료구조 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서x, 중복x, 수정o, 삭제o

# key, value (Json) -> MongoDB
# 선언
a = {'name': 'kim', 'phone': '010-7777-7777', 'birth': 870214}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr': [1, 2, 3, 4, 5]}

print(a['name'])
# print(a['name1']) 에러
print(a.get('name'))
print(a.get("address"))
print(c['arr'][1:2])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = (1, 2,  3,)

# keys, values, items(dict 전체)
print(a.keys())
# list처럼 생겼지만 리스트가 아님
print(type(a.keys()))
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a. values())
print(list(a.values()))

print(a.items())
print(list(a.items()))

print(1 in b)
print(2 in b)

print('name2' not in a)



# 집합(Sets) (순서x, 중복x)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)

# 슬라이싱 가능 + 주로 변환해서 사용

t = tuple(b)
print(t)
l = list(b)
print(l)

print()
print()
print()
print()
print()
print()

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1.intersection(s2))
print(s1 & s2)

print(s1 | s2)
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2))

s3 = set([7, 8, 10 ,15])
s3.add(18)
print(s3)

s3.add(7)
print(s3)

s3.remove(15)
print(s3)

print(type(s3))
