# 1주차 코드 과제
#

# 1번
star = '*'
i = 0
while i < 9:
    i += 1
    if i % 3 == 0:
        continue
    print(star * i)
# 2번
q2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

q2 = list(map(lambda x: str(int(x)+1), q2))
print('q2 = ', q2)

# 3번
a = ['base ball', 'basket ball', 'soccer', 'soccer']

b = {}
for elem in a:
    if b.get(elem) == None:
        b[elem] = 1
    else:
        b[elem] += 1

for key in b:
    print(key, b.get(key))

# 4번
a = 0
for num in range(12):
    print(a, end=' ')
    if num > 8:
        num = 8
    a = 2**num
    

# for num in range(0:10):
#     num

