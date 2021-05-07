# 펠린드롬

def solution(s):
    if s[::-1] == s:
        return '빈문자열'
    else:
        h = len(s)//2
        s1 = s[:h]
        return s1+s1[::-1]

print(solution('abcdcba'))
print(solution('bannana'))
print(solution('wabe'))
