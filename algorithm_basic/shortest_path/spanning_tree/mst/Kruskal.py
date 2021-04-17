# 크루스칼 알고리즘
# 탐욕알고리즘을 기반으로 목적에 맞는 노드를 선택
# 선택하면서 사이클이 생기는지를 UNION FIND기법으로 확인

# UNION FIND 
# 노드를 선택하면서 두 노드의 ROOT 노드가 같은지를 확인
# 노드가 연결된 구조가 링크드 리스트가 될 가능성이 높아짐
# -> O(N)의 시간복잡도가 적합하지 않아
# 결론 : UNION FIND알고리즘까지 최적화를 해야함

graph = {
    'vetices':['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges':[
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (9, 'B', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (5, 'E', 'C'),
        (7, 'E', 'B'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

parent = dict()
rank = dict()


def find(node):
    # path compression
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2

        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(graph):
    mst = list()
    # 1.초기화
    for node in graph['vetices']:
        make_set(node)

    # 2.간선 weight 기반 sorting
    edges = graph['edges']
    edges.sort()
    
    # 3.간선 연결(사이클 확인)
    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v)!=find(node_u):
            union(node_v, node_u)
            mst.append(edge)

    return mst

print(kruskal(graph))
