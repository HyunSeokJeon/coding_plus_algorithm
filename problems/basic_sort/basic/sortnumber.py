# 수 정렬하기

import sys

n = int(sys.stdin.readline())
data = dict()
for i in range(1, 10001):
    data[i] = 0

for i in range(n):
    data[int(sys.stdin.readline())] += 1

for i in data.keys():
    for j in range(data.get(i)):
        print(i)