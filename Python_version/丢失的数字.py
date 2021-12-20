class Solution:
    def miss_number(self,nums):
        xor = 0
        for i,num in enumerate(nums):
            xor ^= num ^ i
        return xor ^ len(nums)
