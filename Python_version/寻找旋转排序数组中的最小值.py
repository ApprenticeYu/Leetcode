class Solution:
    def find_min(self,nums):
        low,high = 0,len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < nums[high]:
                mid = high
            else:
                low = mid + 1
        return nums[low]
