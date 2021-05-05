# 숫자를 뒤집어라

class Solution:
    def reverse(self, x: int) -> int:
        sign = False
        if x<0:
            x = -x
            sign = True
        a = list(str(x))
        a.reverse()
        a = int(''.join(a))
        if sign:
            a = -a
        if a < -2**31 or a > 2**31-1:
            return 0
        return a
        


x = Solution()
print(x.reverse(1534236469))