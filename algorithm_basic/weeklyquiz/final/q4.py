# 퇴사전 빡세게 일하자

def solution(N, duration, cost):
    dp = [0]*(N+1)
 
    def dynamic_programming():
        max_val = 0
        for i in range(N-1, -1, -1):
            if i+duration[i] > N:
                continue
            comp = dp.copy()
            # comp[i] = 1
            # for j in range(i, i+duration[i]):
            #     comp[j] = 0
            # sumdp = 0
            # sumcomp = 0
            # for j in range(i, N+1):
            #     sumdp += dp[j] * cost[j]
            #     sumcomp += comp[j] * cost[j]
            # if sumdp < sumcomp:
            #     dp = comp

            print(dp)
            print('duration',duration[i])
            print('cost', cost[i])
            print(i)
 
        return max_val
 
    result = dynamic_programming()
    return result
 
 
N = 7
duration = [3, 5, 1, 1, 2, 4, 2]
cost = [10, 20, 10, 20, 15, 40, 200]
print(solution(N, duration, cost))
 
N = 10
duration = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
cost = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50]
print(solution(N, duration, cost))