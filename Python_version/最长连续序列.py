class Solution:
    def longest_consecutive(self,nums):
        nums_set = set(nums)
        longest = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = nums
                current = 1
                while num + 1 in nums_set:
                    current_num += 1
                    current += 1
                longest = max(longest,current)
        return longest
