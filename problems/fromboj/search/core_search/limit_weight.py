# 중량제한

import sys
n, m = list(map(int, sys.stdin.readline().strip().split()))

ill = {node:0 for node in range(1,n+1)} # islands list

def pushdict(a, b, c):
    if a in edges:
        if b in edges[a]:
            edges[a][b] = max(edges[a][b], c)
        else:
            edges[a][b] = c
    else:
        edges[a] = dict()
        edges[a][b] = c

edges = dict()
for _ in range(m):
    a, b, c = list(map(int, sys.stdin.readline().strip().split()))
    pushdict(a, b, c) 
    pushdict(b, a, c)
start, end = list(map(int, sys.stdin.readline().strip().split()))

def bfs(start, end):
    connected = list()
    need_connect = list()
    need_connect.append(start)
    while need_connect:
        current_node = need_connect.pop()
        if current_node not in connected:
            connected.append(current_node)
            current_node_nexts = list(edges.get(current_node).keys())
            need_connect.extend(current_node_nexts)
            for i in current_node_nexts:
                if edges.get(current_node).get(i) > ill[i]:
                    ill[i] = edges.get(current_node).get(i)
    return ill.get(end)
                
print(bfs(start, end))

# 시간초과


