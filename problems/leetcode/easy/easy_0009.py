# 회문 True

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        b = list(str(x))
        b.reverse()
        b = int(''.join(b))
        if x == b:
            return True
        return False

a = Solution()
print(a.isPalindrome(-101))