testcase = int(input())

def find(x):
    if x == parent[x]:
        return x
    else :
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        number[x] += number[y]


for _ in range(testcase):
    F = int(input())
    parent = dict()
    number = dict()
    for __ in range(F):
        a, b = input().split(' ')
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1
        union(a, b)
        print(number[find(a)])


