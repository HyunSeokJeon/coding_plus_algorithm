# 로마 숫자 번역

class Solution:
    def romanToInt(self, s: str) -> int:
        r = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        sum = 0
        ml = list()
        for i in range(len(s)):
            sum += r[s[i]]
            if i != 0:
                if r[s[i-1]] < r[s[i]]:
                    ml.append(s[i-1])
        for i in ml:
            sum -= 2 * r[i]
        return sum

x = Solution()
print(x.romanToInt("MCMXCIV"))