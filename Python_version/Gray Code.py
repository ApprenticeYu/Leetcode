class Solution:
    def Gray_Code(self,n):
        ans,head = [0],1
        for i in range(n):
            for j in range(len(ans) - 1,-1,-1):
                ans.append(head + ans[j])
            head <<= 1
        return ans
