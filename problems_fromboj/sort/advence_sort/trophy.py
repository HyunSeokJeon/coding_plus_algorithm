# 트로피 진열

import sys

n = int(sys.stdin.readline())
max = 0
cnt = 0
c = list()
for i in range(n):
    c.append(int(sys.stdin.readline())) 
for i in c:
    if max < i:
        max = i
        cnt += 1
print(cnt)
max = 0
cnt = 0

while len(c) != 0:
    i = c.pop()
    if max < i:
        max = i
        cnt += 1
print(cnt)
