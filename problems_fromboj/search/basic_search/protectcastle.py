# 성 지키기

import sys

n, m = map(int, sys.stdin.readline().strip().split())
a = []
for _ in range(n):
    a.append(input())

row = [0] * n
column = [0] * m

for i in range(n):
    for j in range(m):
        if a[i][j] =='X':
            row[i] = 1
            column[j] = 1

row_count = 0
for i in range(n):
    if row[i] == 0:
        row_count += 1
column_count = 0
for j in range(m):
    if column[j] == 0:
        column_count += 1


print(max(row_count,column_count))