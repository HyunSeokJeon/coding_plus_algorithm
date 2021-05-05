# 과제3

s1 = 'aabcc'
s2 = 'dbbca'
s3 = 'aadbbcbcac'
# print(s3.index('a'))
# print(s3.index('a', 1))
# print(s3.index('b', 2))
# print(s3.index('c', 4))
# print(s3.index('c', 6))
# index = 0
# answer = True
# for i in s2:
#     if index > s3.index(i, index):
#         answer= False
#     print(s3.index(i, index))
#     index = s3.index(i, index) + 1
# print(answer)


def solution(s1, s2, s3):
    if len(s3) <= 1:
        if s1 + s2 == s3:
            return True
        return False
    if len(s3) != len(s1)+len(s2):
            return False
    for i in s1:
        if i not in s3:
            return False
        
    for i in s2:
        if i not in s3:
            return False
    return True
print(solution(s1, s2, s3))


# for i in range(1,len(s2)):
#     try:
#         i1 = s3.index(s2[i], a)
#         i2 = s3.index(s2[i-1],a)
#     except ValueError:
#         answer = False
#         break
        
#     print(i1, i2)
#     if i2 <= i1:
#         a = i1
#     else:
#         answer = False
#         break
# print(answer)


s1 = 'aabcc'
s2 = 'dbbca'
s3 = 'aadbbcbcac'
ifif = 0
l = 0
r = 0
i = 0
ans = True
while i != len(s3):
    print(i, l, r)
    if s3[i] == s1[l] and s3[i] == s2[r]:
        pass
        l2 = l
        r2 = r
        i1 = i
        i2 = i
        while s3[i1] == s1[l2]:
            if len(s1)-1 == l2:
                break
            i1 += 1
            l2 += 1
        while s3[i2] == s1[r2]:
            if len(s2)-1 == r2:
                break
            i2 += 1
            r2 += 1
        if r2-r > l2-l :
            r = r2
            i = i2
        else:
            l = l2
            i = i1
    elif s3[i] == s1[l] and s3[i] != s2[r]:
        while s3[i] == s1[l]:
            if len(s1)-1 == l:
                i+=1
                break
            i+=1
            l+=1
            
    elif s3[i] != s1[l] and s3[i] == s2[r]:
        while s3[i] == s2[r]:
            if len(s2)-1 == l:
                i+=1
                break
            i+=1
            r+=1
    else:
        ans = False
    if ifif>20:
        break
    ifif+=1
    
