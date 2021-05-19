

a = [[1,1]]
print(a[-1])

a = [[1,1],[1,2],[1,3]]
if len(a) != 1:
    for i in range(len(a)-1, 0, -1):
        a[i] = a[i-1].copy()
print(a)
a[0][0] = a[0][0] + 1
print(a)

b = len(a)
a.append(1)
print(a)
print(b)