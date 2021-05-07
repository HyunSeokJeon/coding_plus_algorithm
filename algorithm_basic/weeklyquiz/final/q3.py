# k번째 수

array = [1,5,2,6,3,7,4]
print(sorted(array[2-1:5])[3-1])

def solution(array, commands):
    answer = []
    for n in commands:
        answer.append(sorted(array[n[0]-1:n[1]])[n[2]-1])

    return answer