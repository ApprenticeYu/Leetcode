class Solution:
    def duplicate_nums(self,nums,k):
        ans = list()
        for num in nums:
            if ans.count(num) != 0:
                return True
            ans.append(num)
            if len(ans) > k:
                ans.pop(0)
        return False

result = Solution()
print(result.duplicate_nums([1,2,3,1,2,3],2))
