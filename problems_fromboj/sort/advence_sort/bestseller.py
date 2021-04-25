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
b = [(cnt, book) for book, cnt in a.items()]
b.sort(key=lambda x:x[0], reverse=True)
candidate = b.pop(0)
while len(b) != 0:
    cal = b.pop(0)
    if cal[0] == candidate[0]:
        if candidate[1][0] > cal[1][0]:
            candidate = cal
    else:
        break
print(candidate[1])