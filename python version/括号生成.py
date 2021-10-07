class Solution:
    def create(self,n):
        ans = list()
        def back(S,left,right):
            if len(S) == 2 * n:
                ans.append(" ".join(S))
                return
            if left < n:
                S.append("(")
                back(S,left + 1,right)
                S.pop()
            if right < left:
                S.append(")")
                back(S,left,right + 1)
                S.pop()
        back([],0,0)
        return ans

result = Solution()
print(result.create(1))
