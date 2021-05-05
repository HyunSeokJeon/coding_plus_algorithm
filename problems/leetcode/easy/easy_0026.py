# 정렬된 값에서 중복된 값을 지워보자



class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[cnt] = nums[i]
                cnt+=1
        return cnt

x = Solution()
print(x.removeDuplicates([1,1,2]))