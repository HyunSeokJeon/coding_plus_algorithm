# 외벽점검

from itertools import permutations

def solution(n, weak, dist):
    answer = 0
    l = len(weak)
    cdi = []
    wp = weak+ [w+n for w in weak]
    print(wp)
    
    for i in range(len(weak)):
        for j in permutations(dist):
            count = 1
            pos = weak[i]
            for k in j:
                pos += k

                if pos < wp[i+l-1]:
                    count += 1

                    pos = [w for w in wp[i+1:i+l] if w > pos][0]
                else:
                    cdi.append(count)
                    break
    
    if len(cdi) == 0 :
        return -1
    else:
        return min(cdi)

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))
 
n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]
print(solution(n, weak, dist))