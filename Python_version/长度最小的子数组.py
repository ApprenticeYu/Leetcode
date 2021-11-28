class Solution:
    def min_subarray(self,s,nums):
        if not nums:
            return 0
        start = 0
        end = 0
        total = 0
        n = len(nums)
        ans = n + 1
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans,end - start + 1)
                total -= nums[start]
                start += 1
            end += 1
        return 0 if ans == n + 1 else ans
