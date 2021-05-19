# 

k = 3
num = [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1]	
links = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]


def solution(k, num, links):
    tree = {i:[] for i in num}
    for i in range(len(links)):
        l, r = links[i]
        if l != -1:
            tree[i] 

    answer = 0
    return answer