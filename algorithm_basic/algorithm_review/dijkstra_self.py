mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

import heapq

def dijkstra(graph, start_node):
    distances = {node:float('inf') for node in graph.keys()}
    distances[start_node] = 0
    print(distances)
    need_visit = list()
    heapq.heappush(need_visit, [distances[start_node], start_node])
    while need_visit:
        current_distance, current_node = heapq.heappop(need_visit)

        if current_distance <= distances[current_node]:
            for adjacent, weight in graph[current_node].items():
                distance = current_distance + weight

                if distance < distances[adjacent]:
                    distances[adjacent] = distance
                    heapq.heappush(need_visit, [distance, adjacent])
    return distances


print(dijkstra(mygraph, 'A'))