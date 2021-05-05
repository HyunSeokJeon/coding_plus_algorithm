# 트리의 높이와 너비
import sys
n = int(sys.stdin.readline())

nodelist = dict()
levellist = {i:[] for i in range(1, 101)}

for _ in range(n):
    node, left, right = list(map(int, sys.stdin.readline().split()))
    if node not in nodelist:
        nodelist[node] = [node]
    nodelist[node].extend([left, right])
    if left != -1:
        nodelist[left] = [node]
        a = left
        cnt = 1
        while a != 1:
            a = nodelist[a][0]
            cnt+=1
        levellist[cnt].append(left)
    if right != -1:
        nodelist[right] = [node]
        a = right
        cnt = 1
        while a != 1:
            a = nodelist[a][0]
            cnt+=1
        levellist[cnt].append(right)

# 중위탐색
connected = list()
need_connect = list()
start = 1
while nodelist.get(start)[1] != -1:
    start = nodelist.get(start)[1]
need_connect.append(start)
while need_connect:
    if len(connected) == n:
        break
    current_node = need_connect.pop()
    while nodelist.get(current_node)[1] != -1 and nodelist.get(current_node)[1] not in connected:
        current_node = nodelist.get(current_node)[1]
    if current_node not in connected:
        connected.append(current_node)
        if nodelist.get(current_node)[2] == -1:
            need_connect.append(nodelist.get(current_node)[0])
        else:
            need_connect.append(nodelist.get(current_node)[2])
    else:
        need_connect.append(nodelist.get(current_node)[0])
max_index = 0
max_witdh = 0
for i in levellist.keys():
    if len(levellist.get(i)) <= 1:
        continue
    levellist.get(i).sort()
    st = levellist.get(i)[0]
    en = levellist.get(i)[-1]

    st_index = connected.index(st)
    en_index = connected.index(en)
    if max_witdh < (en_index - st_index + 1):
        max_index = i
        max_witdh = en_index - st_index + 1

print(max_index, max_witdh)