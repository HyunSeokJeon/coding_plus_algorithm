# 트리 순회

n = int(input())

nodelist = dict()
nodelist['A'] = ['A']
for _ in range(n):
    node, left, right = list(input().split())
    nodelist[node].extend([left, right])
    if left != '.':
        nodelist[left] = [node]
    if right != '.':
        nodelist[right] = [node]

# 전위순회
connected = list()
need_connect = list()
need_connect.append('A')
while need_connect:
    current_node = need_connect.pop(0)
    if current_node not in connected:
        connected.append(current_node)
        temp = list(nodelist.get(current_node))
        root = temp.pop(0)
        temp.reverse()
        for i in temp:
            if i =='.':
                continue
            need_connect.insert(0,i)
print(''.join(connected))

# 중위 순회
connected = list()
need_connect = list()
start = "A"
b = 0
while nodelist.get(start)[1] != '.':
    start = nodelist.get(start)[1]
need_connect.append(start)
while need_connect:
    current_node = need_connect.pop()
    while nodelist.get(current_node)[1] != '.' and nodelist.get(current_node)[1] not in connected:
        current_node = nodelist.get(current_node)[1]
    if current_node not in connected:
        connected.append(current_node)
        if nodelist.get(current_node)[2] == '.':
            need_connect.append(nodelist.get(current_node)[0])
        else:
            need_connect.append(nodelist.get(current_node)[2])
    else:
        need_connect.append(nodelist.get(current_node)[0])
    if len(connected) == len(nodelist.keys()):
        break

print(''.join(connected))

# 후위 순회
connected = list()
need_connect = list()
need_connect.append(start)
b = 0
while need_connect:
    current_node = need_connect.pop()
    while nodelist.get(current_node)[1] != '.' and nodelist.get(current_node)[1] not in connected:
        current_node = nodelist.get(current_node)[1]
    a = list(nodelist.get(current_node))
    if (a[1] in connected or a[1] == '.') and (a[2] in connected or a[2] == '.') and current_node not in connected:
        
        connected.append(current_node)
        need_connect.append(a[0])
    else:
        if nodelist.get(current_node)[2] == '.':
            need_connect.append(nodelist.get(current_node)[0])
        else:
            need_connect.append(nodelist.get(current_node)[2])
    if len(connected) == len(nodelist.keys()):
        break
    
print(''.join(connected))