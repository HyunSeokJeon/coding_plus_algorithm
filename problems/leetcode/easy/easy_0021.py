# 가장 긴 공통 문자

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        #이진탐색을 써보자
        alen, a = min(map(lambda x:[len(x), x] , strs))
        mx = len(a)
        mn = 0
        answer = ''
        mid = (len(a) + mn) // 2
        while mn != mid or mx != mid:
            mid = (mx + mn) // 2
            judge = False
            for i in range(alen-mid):
                print(a[i:i+mid])
                for j in strs:
                    if a[i:i+mid] in j:
                        answer = a[i:i+mid]
                        judge = True
            if judge:
                mn = (mid + mn) // 2
            else:
                mx = (mx + mid) // 2
        
        return answer


x = Solution()
y = x.longestCommonPrefix(["flower","flow","flight"])
print(len(y), y)
a = ["flower","flow","flight"]
b = min(map(lambda x:[len(x), x] , a))
print(b)
# 다음에 다시해보자