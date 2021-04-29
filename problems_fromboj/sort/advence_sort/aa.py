a = dict()
from collections import defaultdict

a = {1: {2: 4, 3: 3}, 2: {1: 4, 3: 2}, 3: {1: 3, 2: 2}}

print(list(a.get(1).keys()))

a = [1, 2, 3]
root, b = a
print(root)
b = [9, 99]
a.pop(0)
b.reverse()
for i in b:
    a.insert(0, i)

print(a)