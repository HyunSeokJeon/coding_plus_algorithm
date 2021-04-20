# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1 
# 8 1 7 2 6 3 5 4

a = input()

def scale(string):
    a = string.split()  
    b = []
    b.extend(a)
    answer = ''
    b.sort()
    if a==b:
        answer = 'ascending' 
        return answer
    b.sort(reverse=True)
    if a==b:
        answer = 'descending'
        return answer

    answer = 'mixed'
    return answer


print(scale(a))