


n = 4
a = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
b = {i:[] for i in range(1, n+1)}
for i in a:
    b[i[0]].append([i[1],i[2], True])
    b[i[1]].append([i[0],i[2], False])

print(b)

import heapq

def solution(n, start, end, roads, traps):
    roots = {i:[] for i in range(1, n+1)}
    for i in roads:
        roots[i[0]].append([i[1], i[2], True])
        roots[i[1]].append([i[0], i[2], False])

    queue.

    r_time = {i:float('inf') for i in range(1, n+1)}
    n_con = list()
    r_time[start] = 0
    n_con.append([start, r_time[start]], True)
    while n_con:
        c_node, c_time, c_avl = n_con.pop()
        if r_time[c_node] < c_time:
            continue
        for node, time, avl in 
            


    answer = 0
    return answer