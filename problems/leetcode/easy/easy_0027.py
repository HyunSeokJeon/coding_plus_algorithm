# 

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[cnt] = nums[i]
                cnt += 1
        print(nums)
        return cnt
x = Solution()
print(x.removeElement([0,1,2,2,3,0,4,2], 2))