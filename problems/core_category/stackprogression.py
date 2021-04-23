# 스택수열
# n = int(input())

# nlist = list()
# for aa in range(n):
#     nlist.append(int(input()))
# print(nlist)
n = 8
nlist = [4, 3, 6, 8, 7, 5, 2, 1]

zeroton = list(range(1,n+1))
print(zeroton)
stack = list()
nlist_clone=list()
answerlist = list()
index = 0
while True:
    var1 = zeroton.pop(0)
    if nlist[index] != var1:
        stack.append(var1)
        answerlist.append('+')
    else:
        stack.append(var1)
        answerlist.append('+')
        nlist_clone.pop()
        answerlist.append('-')
    index += 1
    if(index == len(nlist)):
        break
print(answerlist)


