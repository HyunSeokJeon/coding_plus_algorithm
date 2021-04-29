# 큰수 찾기


# 병합정렬
def mergesort(numbers):
    if len(numbers) <= 1:
        return numbers
    mid = len(numbers) // 2
    left = mergesort(numbers[:mid])
    right = mergesort(numbers[mid:])
    li, ri = 0, 0
    returnlist =list()
    while len(left) > li and len(right) > ri:
        if left[li]+right[ri] > right[ri]+left[li]:
            returnlist.append(left[li])
            li+=1
        else:
            returnlist.append(right[ri])
            ri+=1
    while len(left) > li:
        returnlist.append(left[li])
        li += 1
    while len(right) > ri:
        returnlist.append(right[ri])
        ri += 1
    
    return returnlist


def solution(numbers):
    numbers = list(map(str, numbers))
    answer = (''.join(mergesort(numbers)))
    while answer[0] == '0':
        if len(answer) == 1:
            break
        answer = answer[1:]
    return answer
# print(solution([0, 0, 0, 0, 0, 0]))
# print(solution([1, 11, 111, 1111]))
print(solution([90,908,89,898,10,101,1,8,9]))

# [10, 101] "10110"
# [1, 11, 111, 1111] "1111111111"
# [0, 0, 0, 0, 0, 0] "0"


