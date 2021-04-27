# 중량제한
n, m = list(map(int, input().split()))

maxw = 0
minw = 1000000000

for _ in range(n):
    a, b, c = list(map(int, input().split()))
    if c < minw:
        minw = c
    if c > maxw:
        maxw = c
    
while minw <= maxw:
    c < minw 





start, end = list(map(int, input().split()))