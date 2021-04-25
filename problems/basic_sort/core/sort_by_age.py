# 나이순 정렬
import sys

N = int(sys.stdin.readline())
data = []
for i in range(N):
    data.append(sys.stdin.readline().strip().split())
data.sort(key=lambda x:int(x[0]))
for i in data:
    print(' '.join(i))