# 가장 큰 증가 부분수열
n = 10
a = '1 100 2 50 60 3 5 6 7 8'.split()
maxsum = 0
dp = [0 for _ in range(n)]
for i in range(1, n):
    for j in range(0, i-1):
        if dp[j] < dp[i]:
            dp[i] = max