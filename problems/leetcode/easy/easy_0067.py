# 숫자가 한자리씩 배열로 주어짐
# 1을 더한 값을 배열로 반환하라

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin((int("0b"+ a, 2)+ int("0b"+b,2)))[2:])


x = Solution()
print(x.addBinary("1010", "1011"))

