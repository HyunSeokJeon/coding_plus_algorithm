N, M, V = 4, 5, 1
edges = [[1, 2], [1, 3], [1,4], [2, 3], [3, 4]]
def solution(N, M, V, edges):
    edgedict = {a:[] for a in range(1, N+1)}
    for v1, v2 in edges:
        edgedict[int(v1)].append(int(v2))
        edgedict[int(v2)].append(int(v1))
    
    def printa(answer):
        returnstr = ''
        for n in answer:
            returnstr += (str(n) + ' ')
        return returnstr.strip()
    visited = list()
    def dfs(start):
        need_visit = list()
        need_visit.append(start)
        while need_visit:
            current_node = need_visit.pop()
            if current_node not in visited:
                visited.append(current_node)
                a = edgedict.get(current_node)
                a.sort(reverse=True)
                need_visit.extend(edgedict.get(current_node))
    dfs(V)           

    return printa(visited)
solution(N, M, V, edges)
