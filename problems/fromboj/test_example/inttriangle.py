# 정수삼각형
# dp[i][j] : 도착했을때 최대값
# dp[i][j] : max(dp[i-1][j-1], dp[i-1][j] + a[i][j])
n = int(input())
a = [[0 for _ in range(n+1)] for _ in range(n+1) ]
dp = [[0 for _ in range(n+1)] for _ in range(n+1) ]

for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    for j in range(1, i+1):
        a[i][j] = tmp[j-1]

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + a[i][j]


print(max(dp[n]))