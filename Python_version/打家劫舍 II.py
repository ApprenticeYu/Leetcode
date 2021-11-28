class Solution:
    def rob(self,nums):
        def rob_range(start,end):
            first = nums[start]
            second = max(nums[start],nums[start + 1])
            for i in range(start + 2,end + 1):
                first = second
                second = max(first + nums[i],second)
            return second
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        return max(rob_range(0,n - 2),rob_range(1,n - 1))
