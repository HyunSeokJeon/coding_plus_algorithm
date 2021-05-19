# 어피치의 소비습관

def solution(gems):
    gemset = set(gems)
    size = len(gemset)
    candidate = list()
    for start in range(len(gems)):
        a = set()
        for i in range(start,len(gems)):
            a.add(gems[i])
            if len(a) == size:
                candidate.append([start+1, i+1, i-start])
    answer = sorted(candidate, key=lambda x:x[2])[0]
    return answer[:2]

def solution(gems):
    g_dict = {i:[] for i in gems}
    for i in range(len(gems)):
        g_dict[gems[i]].append(i)
    print(g_dict)
    
    
 
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))
 
gems = ["AA", "AB", "AC", "AA", "AC"]
print(solution(gems))
 
gems = ["XYZ", "XYZ", "XYZ"]
print(solution(gems))
 
gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))