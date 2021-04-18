# n개의 노드가 있는 그래프가 있다. 
# 각 노드는 1부터 n까지 번호가 적혀있다. 
# 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 한다. 
# 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 
# 간선의 개수가 가장 많은 노드들을 의미한다.

# 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 
# 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 
# solution 함수를 작성하라.

# 제한사항

# 노드의 개수 n은 2 이상 20,000 이하입니다.
# 간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
# vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.

import heapq
from collections import defaultdict

vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
n = 6

def solution(n, vertex):
    distances = {node:float('inf') for node in range(1,n+1)}
    distances[1] = 0

    edges = defaultdict(list)
    for node_s, node_e in vertex:
        edges[node_s].append(node_e)
        edges[node_e].append(node_s)
    
    todo_visit = list()
    heapq.heappush(todo_visit, [distances[1], 1])

    while todo_visit:
        current_distance, current_node = heapq.heappop(todo_visit)

        if distances[current_node] < current_distance:
            continue
        
        for node in edges[current_node]:
            distance = current_distance + 1
            if distance < distances[node]:
                distances[node] = distance
                heapq.heappush(todo_visit, [distance, node])
                
    max_distance = 0
    max_distance_cnt = 0
    for distance in distances.values():
        if max_distance < distance:
            max_distance = distance
            max_distance_cnt = 1
        elif max_distance == distance:
            max_distance_cnt += 1

    return max_distance_cnt


