class Solution:
    def once_number(self,nums):
        total = 0
        for num in nums:
            total ^= num
        pos = total & (-total)
        total1 = 0
        total2 = 0
        for num in nums:
            if pos & num:
                total1 ^= num
            else:
                total2 ^= num
        return [total1,total2]
