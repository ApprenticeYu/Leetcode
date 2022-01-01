class Solution:
    def total(self,nums,target):
        dp = [1] + [0] * target
        for i in range(1,target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
        return dp[target]
