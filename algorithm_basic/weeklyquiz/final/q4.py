# 퇴사전 빡세게 일하자

def solution(N, duration, cost):
    dp = [0]*(N+1)
 
    def dynamic_programming():
        max_val = 0
        sumdp = 0
        sumcomp = 0
        for i in range(N-1, -1, -1):
            if i+duration[i] > N:
                continue
            comp = dp.copy()
            comp[i] = 1
            for j in range(i+1, i+duration[i]):
                comp[j] = 0
            sumdp = 0
            sumcomp = 0
            for j in range(len(comp)-1):
                sumdp += dp[j] * cost[j]
                sumcomp += comp[j] * cost[j]
            if sumdp <= sumcomp:
                dp[i] = 1
                for j in range(i+1, i+duration[i]):
                    dp[j] = 0
            print(comp)
    
    result = dynamic_programming()
    sumdp = 0; 
    for i in range(len(dp)-1):
        sumdp += dp[i] * cost[i]
    result = sumdp
    return result

N = int(input())
duration = []
cost = []
for _ in range(N):
    d, c = list(map(int,input().split()))
    duration.append(d)
    cost.append(c)
 
print(solution(N, duration, cost))

5
3 50
1 1
3 3
2 2 
1 1