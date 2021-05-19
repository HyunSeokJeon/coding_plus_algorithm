# 

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = s.split(" ")
        answer = 0
        for a in range(-1, -len(n)-1,-1):
            if n[a] != "":
                answer = len(n[a])
                break
        return answer
        

x = Solution()
print(x.lengthOfLastWord("Today is a nice day"))