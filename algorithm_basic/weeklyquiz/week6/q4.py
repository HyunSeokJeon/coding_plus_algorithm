import heapq


def solution(x):
    x1 = [[-a, a] for a in x]
    heapq.heapify(x1)
    return heapq.heappop(x1)[1]


a = [-1, -1, -1, -1, 0, 1, 20, 19, 17]
print(solution(a))
