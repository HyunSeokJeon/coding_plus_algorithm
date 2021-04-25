# 좌표 정렬하기
import sys

N = int(sys.stdin.readline())
data = []
for _ in range(N):
    data.append(tuple(map(int,sys.stdin.readline().split())))

data.sort()
for i in data:
    print(i[0], i[1])