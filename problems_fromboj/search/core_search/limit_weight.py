# 중량제한

n, m = list(map(int, input().split()))

ill = dict()
for i in range(1, n+1):
    ill[i] = 0

edges = dict()
for _ in range(n):
    a, b, c = list(map(int, input().split()))
    if a in edges:
        edges[a].append((b, c))
    else:
        edges[a] = [(b, c)]
    
print(edges)


start, end = list(map(int, input().split()))

