class Solution:
    def is_power_of_two(self,n):
        return n > 0 and (n & (n - 1)) == 0
