def solution(n):
    sum = 0
    for i in str(n):
        sum+= int(i)**2
    if sum == 1:
        return True
    if sum == 4:
        return False
    return solution(sum)

# Test code
print(solution(19)) # True
print(solution(61)) # False


