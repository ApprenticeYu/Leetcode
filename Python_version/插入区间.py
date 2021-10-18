class Solution:
    def insert(self,original,new):
        ans = []
        n = len(original)
        place = False
        left,right = new
        for i in range(n):
            li,ri = original[i]
            if right < li:
                if not place:
                    ans.append([left,right])
                    place = True
                ans.append([li,ri])
            elif ri < left:
                ans.append([li,ri])
            else:
                left = min(li,left)
                right = max(ri,right)
        if not place:
            ans.append([left,right])
        return ans

result = Solution()
original = [[1,5]]
new = [2,7]
print(result.insert(original,new))
