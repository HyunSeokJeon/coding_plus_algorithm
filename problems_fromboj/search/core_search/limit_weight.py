# 중량제한

n, m = list(map(int, input().split()))

ill = {node:0 for node in range(1,n+1)}



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
    a, b, c = list(map(int, input().split()))
    pushdict(a, b, c) 
    pushdict(b, a, c)
    
print(edges)
print(ill)
start, end = list(map(int, input().split()))

result = 0
# def bfs(start):
#     connected = list()
#     need_connect = list()
#     need_connect.append(start)
#     while need_connect:
#         current_node = need_connect.pop(0)
#         result = 0 
#         if current_node not in connected:
#             connected.append(current_node)
#             need_connect.extend(list(edges.get(current_node).keys()))

