# 괄호가 잘 닫혀있는지 확인해보자

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        part = {'(':')', '{':'}', '[':']'}
        expect = list()
        cnt = 0
        for i in s:
            if i in part.keys():
                cnt += 1
                expect.append(part[i])
            else:
                if expect:
                    if i == expect.pop():
                        cnt -= 1
                        continue
                    else:
                        return False
                else:
                    return False
        if cnt != 0:
            return False
        return True

x = Solution()
print(x.isValid("{{{{"))