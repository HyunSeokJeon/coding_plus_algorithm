def solution(a):
    if len(a[0]) == 0:
        return 0
    for i in range(len(a)-1):
        if a[0] == a[i+1][0:len(a[0])]:
            continue
        else:
            a[0] = a[0][0:-1]
            return solution(a)
    return len(a[0])
    
    
    
 
# Test code
print(solution(['abcd', 'abce', 'abchg', 'abcfwqw', 'abcdfg'])) # 3
print(solution(['abcd', 'gbce', 'abchg', 'abcfwqw', 'abcdfg'])) # 0
