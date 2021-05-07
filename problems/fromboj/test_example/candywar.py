# the candy war

t = int(input())
for _ in range(t):
    n = int(input())
    ncase = list(map(int, input().split()))
    answer = 0
    if n == 1:
         print(answer)
         continue
    tmp = ncase.copy()
    while True:
        for i in range(len(ncase)):
            if ncase[i] % 2 == 1:
                ncase[i] += 1
            tmp[i] = ncase[i] // 2
        if len(set(ncase)) == 1:
            print(answer)
            break
        for i in range(len(ncase)):
            ncase[i] = tmp[i]+tmp[i-1]
        answer+=1