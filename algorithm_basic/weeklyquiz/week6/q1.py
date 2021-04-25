# 순열 가지수

import copy

def solution(n, k):
    nlist = list(range(1, n+1))
    cntlist = list()
    answer = list()
    def case(nlist, index, endindex):
        if index == endindex:
            cntlist.append(0)
            if len(cntlist) == k:
                answer.append(list(nlist))
            return nlist
        else:
            for n in range(index, len(nlist)):
                nlist[n], nlist[index] = nlist[index], nlist[n]
                case(nlist, index+1, endindex)
                nlist[n], nlist[index] = nlist[index], nlist[n]
    case(nlist,0,len(nlist)-1)
    return answer[0]

print(solution(4, 9))
    