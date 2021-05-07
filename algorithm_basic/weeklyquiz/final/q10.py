# 어피치의 소비습관

# def solution(gems):
#     gemset = set(gems)
#     size = len(gemset)
#     candidate = list()
#     for start in range(len(gems)):
#         a = set()
#         for i in range(start,len(gems)):
#             a.add(gems[i])
#             if len(a) == size:
#                 candidate.append([start+1, i+1, i-start])
#     answer = sorted(candidate, key=lambda x:x[2])[0]
#     return answer[:2]

def solution(gems):
    g = dict()
    for i in gems:
        if i in g.keys(): g[i] += 1
        else: g[i] = 1
    
    print(min(g,key=lambda x:x.value()))
    
    
    print(g)
 
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))
 
gems = ["AA", "AB", "AC", "AA", "AC"]
print(solution(gems))
 
gems = ["XYZ", "XYZ", "XYZ"]
print(solution(gems))
 
gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))