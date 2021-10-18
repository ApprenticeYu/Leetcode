class Solution:
    def sqrt(self,n):
        if n == 0:
            return 0
        x0,C = float(n),float(n)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi
        return int(xi)

result = Solution()
print(result.sqrt(8))
