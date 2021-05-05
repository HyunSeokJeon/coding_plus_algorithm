
testcase = int(input())

for _ in range(testcase):
    N, M = input().split()
    N = int(N)
    M = int(M)
    queue = list()
    prioritylist = input().split()
    for i in range(N):
        queue.append((int(prioritylist[i]), i))
    
    imax = -1   
    def maxp(queue):
        ma = -1
        for i in queue:
            if i[0] > ma:
                ma = i[0]
        return ma
    imax = maxp(queue)
    count = 1
    a = True
    while a:
        
        if queue[0][0] < imax:
            x = queue.pop(0)
            queue.append(x)
        else:
            if queue[0][1] == M:
                a = False
                print(count)
                break
            queue.pop(0)
            imax = -1
            imax = maxp(queue)
            count+=1
                
