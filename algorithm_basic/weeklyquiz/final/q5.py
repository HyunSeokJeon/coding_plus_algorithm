# 2020 KAKAO BLIND RECRUITMENT

def solution(words, queries):
    answer = []
    for i in queries:
        qmn, l  = i.count('?'), len(i)
        if i[0] =='?':
            test = i[qmn:]
            answer.append(sum(list(map(lambda x: 1 if l==len(x) and x[qmn:] == test else 0, words))))
        else:
            test = i[:-qmn]
            answer.append(sum(list(map(lambda x: 1 if l==len(x) and x[:-qmn] == test else 0, words))))

    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

a = list(map(lambda x: 1 if x[:3]=='fro' and len(x) == 5 else 0, words))
print(a)
print(solution(words, queries))


# trie 알고리즘으로 다시