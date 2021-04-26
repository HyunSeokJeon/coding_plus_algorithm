# 베스트셀러

import sys

n = int(sys.stdin.readline())
a = dict()
for _ in range(n):
    book = sys.stdin.readline().strip()
    if book in a:
        a[book] += 1
    else: 
        a[book] = 1
b = dict()
for book, cnt in a.items():
    if cnt in b:
        b[cnt].append(book)
    else:
        b[cnt] = [book]

maxcnt = 0
for key in b.keys():
    if maxcnt < key:
        maxcnt = key

b[maxcnt].sort()
print(b[maxcnt][0])
