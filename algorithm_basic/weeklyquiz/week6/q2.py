n = 5
number = 200

n5, n5d = divmod(200/5, 11111)

print(n5, n5d)

n4, n4d = divmod(n5d, 1111)
n3, n3d = divmod(n4d, 111)
n2, n2d = divmod(n3d, 11)
n1, n1d = divmod(n2d, 1)

print(n4, n4d)
print(n3, n3d)
print(n2, n2d)
print(n1, n1d)


