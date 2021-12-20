class Solution:
    def optim_occasion(self,prices):
        if not prices:
            return 0
        n = len(prices)
        f0,f1,f2 = -prices[0],0,0
        for i in range(1,n):
            num0 = max(0,f2 - prices[i])
            num1 = f0 + prices[i]
            num2 = max(f1,f2)

            f0,f1,f2 = num0,num1,num2
        return max(f1,f2)
