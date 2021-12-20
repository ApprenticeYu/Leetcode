class Solution:
    def coin_exchange(self,coins,target):
        dp = [float('inf')] * (target + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin,target + 1):
                dp[x] = min(dp[x - coin] + 1,dp[x])
        return dp[target] if dp[target] != float('inf') else -1
