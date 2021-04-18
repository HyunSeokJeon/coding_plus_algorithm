# 프림알고리즘

import heapq

queue = []
graph_data = [[2,'a'], [5, 'b'], [3,'c']]
for edge in graph_data:
    heapq.heappush(queue, edge)

for index in range(len(queue)):
    print(heapq.heappop(queue))

print(queue)

heapq.heapify(graph_data)
for index in range(len(graph_data)):
    print(heapq.heappop(graph_data))

from collections import defaultdict

list_dict = defaultdict(list)
lise_dict = ['key1']
print(list_dict['key1'])
print('------------------------')

edges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')

]

from collections import defaultdict
from heapq import *

def prim(start_node, edges):
    mst = list()
    adjacent_edges = defaultdict(list)
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))
    connected_nodes = set(start_node)
    print(adjacent_edges)
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)
    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))

            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)
    return mst
print(prim('A', edges))