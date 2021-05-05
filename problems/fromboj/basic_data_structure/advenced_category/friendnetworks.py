testcase = int(input())
def bfs(start, networks):
    need_connect = list()
    connected = list()
    need_connect.append(start)
    while need_connect:
        current_node = need_connect.pop(0)
        if current_node not in connected:
            connected.append(current_node)
            need_connect.extend(list(networks[current_node]))

    return connected
for _ in range(testcase):
    F = int(input())
    edges = list()
    networks = dict()
    for __ in range(F):
        a, b = input().split()
        c = [a, b]
        edges.append(c)
        if a not in networks.keys():
            networks[a] = [b]
        else:
            networks[a].append(b)
        if b not in networks.keys():
            networks[b] = [a]
        else:
            networks[b].append(a)
        friendnetwork = bfs(a,networks)
        print(len(friendnetwork))
# 시간초과