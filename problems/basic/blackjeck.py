# 블랙잭

a = input()
b = input()
n, m = a.split(' ')
cardList = b.split(' ')
n = int(n)
m = int(m)
max = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i==j or i==k or j==k:
                continue
            else:
                com = int(cardList[i]) + int(cardList[j]) +int(cardList[k])
                if  max < com and com <= m:
                    max = com
print(max)