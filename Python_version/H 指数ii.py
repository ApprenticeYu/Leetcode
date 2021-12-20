class Solution:
    def H_(self,nums):
        n = len(nums)
        left,right = 0,n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= n - left:
                right = mid - 1
            else:
                left = mid + 1
        return n - left
