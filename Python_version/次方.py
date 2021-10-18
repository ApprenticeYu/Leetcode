class Solution:
    def pow_function(self,x,n):
        def pow_function_core(N):
            ans = 1.0
            x_base = x
            while N:
                if N % 2 == 1:
                    ans *= x_base
                x_base = x_base * x_base
                N //= 2
            return ans
        return pow_function_core(n) if n >= 0 else 1.0 / pow_function_core(-n)

result = Solution()
print(result.pow_function(2.00000,-2))
