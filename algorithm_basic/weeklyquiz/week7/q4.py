

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

def bfs(begin, end, edges):
    dist = {word:float('inf') for word in edges.keys()}
    dist[begin] = 1
    connected = list()
    need_connected = list()
    need_connected.append(begin)
    while need_connected:
        node = need_connected.pop()
        current_dist = dist[node]
        if dist[node] < current_dist:
            continue

        for word in edges[node]:
            distance = current_dist + 1
            if distance < dist[word]:
                dist[word] = distance
                need_connected.append(word)
    if dist[end] == float('inf'):
        return 0
    return dist[end]

def solution(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    edges = {word:[] for word in wordList}
    edges[beginWord] = []
    for i in wordList:
        cnt = 0
        for j in range(len(beginWord)):
            if beginWord[j] != i[j]:
                cnt+=1
        if cnt==1:
            edges[beginWord].append(i)
            edges[i].append(beginWord)

    for i in range(len(wordList)):
        for j in range(i, len(wordList)):
            cnt = 0
            for k in range(len(wordList[i])):
                if wordList[i][k] != wordList[j][k]:
                    cnt+=1
            if cnt == 1:
                edges[wordList[i]].append(wordList[j])
                edges[wordList[j]].append(wordList[i])
            
    if len(edges[endWord]) == 0:
        return 0
    
    a = bfs(beginWord, endWord, edges)

    return a

print(solution(beginWord, endWord, wordList))