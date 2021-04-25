# 피보나치 수

N = int(input())
def solution(N):
    fibonacci = list()
    fibonacci.append(0)
    fibonacci.append(1)
    for i in range(N+1):
        if i==0 or i==1:
            continue
        fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
    return fibonacci[N]
print(solution(N))