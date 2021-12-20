class Solution:
    def bits_count(self,n):
        bit = [0]
        for i in range(1,n + 1):
            bit.append(bit[i & (i - 1)] + 1)
        return bit
