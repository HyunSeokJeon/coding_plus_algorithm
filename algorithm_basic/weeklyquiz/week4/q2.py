def countUniques(a):
    a.sort()
    if(len(a)) == 1:
        return 1
    cnt = 1
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            pass
        else:
            cnt+= 1
    return cnt
            

# Test code
print(countUniques([-1, 1, 1, 1, 1, 4, 4, 4, 4, 10, 14, 14])) # 5
print(countUniques([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1])) # 2