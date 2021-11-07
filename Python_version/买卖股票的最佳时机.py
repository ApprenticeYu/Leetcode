class Solution:
    def optimized_time(self,prices):
        inf = int(1e9)
        max_profit = 0
        min_price = inf
        for price in prices:
            max_profit = max(price - min_price,max_profit)
            min_price = min(price,min_price)
        return max_profit
