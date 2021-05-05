from queue import Queue

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]



def solution(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    edges = {}
    dist = {}
    wordList.append(beginWord)
    f = True
    for i in range(len(wordList)):
        for j in range(i, len(wordList)):
            if f:
                edges[wordList[j]] = []
                dist[wordList[j]] = float('inf')
            cnt = 0
            for k in range(len(wordList[i])):
                if wordList[i][k] != wordList[j][k]:
                    cnt+=1
            if cnt == 1:
                edges[wordList[i]].append(wordList[j])
                edges[wordList[j]].append(wordList[i])
        f = False
            
    if len(edges[endWord]) == 0:
        return 0
    
    dist[beginWord] = 1
    dist[endWord] = -1
    connected = list()
    need_connected = Queue()
    need_connected.put(beginWord)
    while not need_connected.empty():
        node = need_connected.get()
        current_dist = dist[node]
        if abs(dist[node]) < abs(current_dist):
            continue

        for word in edges[node]:
            distance = incr(current_dist)
            if sign(distance) != sign(dist[word]):
                return abs(distance) + abs(dist[word]) -1
            if abs(distance) < abs(dist[word]):
                dist[word] = distance
                need_connected.put(word)

    
    return 0

def sign(x):
    if x>0:
        return 1
    if x<0:
        return -1
    

def incr(x):
    if x>0:
        x+=1
    else:
        x-=1
    return x
print(solution(beginWord, endWord, wordList))

