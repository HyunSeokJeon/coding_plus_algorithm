# 

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        end = len(nums)-1
        start = 0
        while start <= end:
            mid = (end + start) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return start

x = Solution()
print(x.searchInsert([1,3,5,6], 7))