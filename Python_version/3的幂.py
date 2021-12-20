class Solution:
    def is_power_of_three(self,n):
        return n > 0 and 1162261467 % n == 0
