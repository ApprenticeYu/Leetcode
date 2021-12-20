class Solution:
    def 4_power(self,n):
        return n > 0 and (n & (n - 1) == 0) and (n & 0xaaaaaaaa) == 0
