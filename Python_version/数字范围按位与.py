class Solution:
    def bit_and(self,m,n):
        while m < n:
            n &= (n - 1)
        return n
