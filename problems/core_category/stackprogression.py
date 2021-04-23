# 스택수열
# n = int(input())

# nlist = list()
# for aa in range(n):
#     nlist.append(int(input()))
# print(nlist)
# n = 8
# target = [4, 3, 6, 8, 7, 5, 2, 1]
# n=5
# target = [1,2,5,3,4]

n = int(input())
target = list()
for aa in range(n):
    target.append(int(input()))
nlist = list(range(1,n+1))
stack = list()
clone = list()
pmlist = list()
index = 0
while index != n:
    if len(nlist) > 0:
        number = nlist.pop(0)
    if number in stack :
        pmlist = 'NO'
        break
    stack.append(number)
    pmlist.append('+')
    while stack[-1] == target[index]:
        popnumber = stack.pop()
        pmlist.append('-')
        clone.append(popnumber)
        index += 1
        if index ==len(target) or len(stack) == 0:
            break

if type(pmlist) == list:
    for _ in pmlist:
        print(_)
else:
    print(pmlist)


