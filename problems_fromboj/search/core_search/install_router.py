#공유기 설치
import sys

n, c = list(map(int, input().split(' ')))

xlist = []
for i in range(n):
    xlist.append(int(input()))

xlist.sort()
end = xlist[-1] - xlist[0]
start = xlist[1] - xlist[0]
result = 0


while(start <= end):
    mid = (start + end) // 2
    value = xlist[0]
    count = 1
    for i in range(1, len(xlist)):
        if xlist[i] >= value + mid:
            value = xlist[i]
            count += 1
    if count >= c:
        start = mid + 1
        result = mid
    else: 
        end = mid - 1
print(result)
# 다시풀기
