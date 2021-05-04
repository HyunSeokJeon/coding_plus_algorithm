#

def solution(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    edges = {word:[] for word in wordList}
    for i in range(wordList):
        # 그래프로 만들어서
        # 다익스트라 알고리즘

