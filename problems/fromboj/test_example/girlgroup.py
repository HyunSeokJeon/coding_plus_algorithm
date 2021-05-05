# 걸그룹 마스터 준석이
import sys

n, m = list(map(int, sys.stdin.readline().split()))
gdict = dict()
for _ in range(n):
    gname = sys.stdin.readline().strip()
    gdict[gname] = list()
    gnum = int(sys.stdin.readline())
    for _ in range(gnum):
        gdict[gname].append(sys.stdin.readline().strip()) 

answer = ''

for _ in range(m):
    q = sys.stdin.readline().strip()
    qtype = int(sys.stdin.readline())
    if qtype == 1:
        for i in gdict.keys():
            if q in gdict[i]:
                answer += i+'\n'
    elif qtype == 0:
        answer += '\n'.join(sorted(gdict[q]))
        answer += '\n'

print(answer)
