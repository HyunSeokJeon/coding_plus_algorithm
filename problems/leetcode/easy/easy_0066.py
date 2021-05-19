# 숫자가 한자리씩 배열로 주어짐
# 1을 더한 값을 배열로 반환하라

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        arrlen = len(digits)
        num = 0
        for i in range(len(digits)):
            num += digits[i] * 10 ** (arrlen-i-1)
        num += 1
        answer = list()
        for i in str(num):
            answer.append(i)
        return answer

x = Solution()
print(x.plusOne([9,9]))


