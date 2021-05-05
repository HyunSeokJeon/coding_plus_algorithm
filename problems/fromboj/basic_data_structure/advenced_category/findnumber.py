N = int(input())
nlist = set(input().split())
M = input()
mlist = input().split()
for m in mlist:
    setlen = len(nlist)
    nlist.add(m)
    if setlen == len(nlist):
        print(1)
    else:
        print(0)