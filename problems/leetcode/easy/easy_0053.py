# 

class Solution:
    def maxSubArray(self, A: list[int]) -> int:
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
            print(num, curSum, maxSum)

        return maxSum



x = Solution()
print(x.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))