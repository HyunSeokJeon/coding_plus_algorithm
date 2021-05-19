# 퇴사전 빡세게 일하자

def solution(N, duration, cost):
    dp = [0]*(N+1)
 
    def dynamic_programming():
        max_val = 0
        
        avail = list()
        for i in range(N-1, -1, -1):
            if (i + duration[i] > N):
                dp[i] = dp[i+1]
            else:
                dp[i] = max(dp[i+1], cost[i] + dp[i + duration[i]])
                max_val = max(max_val, dp[i])
                print(dp)
        return max_val
    
    result = dynamic_programming()
    return result

N = int(input())    
duration = []
cost = []
for _ in range(N):
    d, c = list(map(int,input().split()))
    duration.append(d)
    cost.append(c)
 
print(solution(N, duration, cost))

# 5
# 3 50
# 1 1
# 3 3
# 2 2 
# 1 1