# nums에서 두 수를 더해 target을 만들 수 있는 인덱스를 찾아라

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            a = target - nums[i]
            if a in nums[i+1:]:
                return [i, nums.index(a, i+1)]

x = Solution()
answer = x.twoSum([3,2,4], 6)
print(answer)