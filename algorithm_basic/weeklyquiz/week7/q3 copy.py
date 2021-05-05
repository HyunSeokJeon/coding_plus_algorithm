from collections import defaultdict
def dfs(s1, s2, s3, i, j, k, dp):
        
    if i in dp and j in dp[i] and k in dp[i][j]:
        return dp[i][j][k]
    
    if k == len(s3) and i == len(s1) and j == len(s2):
        return True
    
    cond1 = False
    if i < len(s1) and k < len(s3) and s1[i] == s3[k]:
        cond1 = dfs(s1, s2, s3, i+1, j, k+1, dp)
    
    cond2 = False
    if j < len(s2) and k < len(s3) and s2[j] == s3[k]:
        cond2 = dfs(s1, s2, s3, i, j+1, k+1, dp)
    
    dp[i][j][k] = cond1 or cond2
    return dp[i][j][k]
    
def isInterleave(s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    
    dp = defaultdict(lambda : defaultdict(lambda : defaultdict(bool)))
    return dfs(s1, s2, s3, 0, 0, 0, dp)

s1 = 'aabcc'
s2 = 'dbbca'
s3 = 'aadbbcbcac'
print(isInterleave(s1, s2, s3))