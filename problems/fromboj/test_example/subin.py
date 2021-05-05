# 수빈이와 수열


n, b =int(input()), list(map(int, input().split()))
answer = list() 
answer.append(b[0])
for i in range(1,n):
    answer.append((i+1)*b[i] - sum(answer))

for i in answer:
    print(i,end=" ")