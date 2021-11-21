class Solution:
    def The_number_of_1(self,n):
        ret = 0
        while n:
            n &= n - 1
            ret += 1
        return ret
