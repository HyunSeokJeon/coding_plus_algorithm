# 1~10번까지

# q6
a = ['파', '이', '썬', '썬', '썬', '썬', '즐', '즐', '즐', '거', '운']
last = None
for elem in a:
    if elem == last:
        continue
    print(elem, end="")
    last = elem
print()

# q7
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = lambda n:n*n
c = list()
for elem in a:
    c.append(b(elem))
print(c)    

# q8
data1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
data2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
result = list(data1[:6]) + data2[::2]
print(result)

# q9
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
c = list(set(a).intersection(set(b)))
print(c)

# q10