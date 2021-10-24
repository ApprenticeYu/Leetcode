class Solution:
    def search_array(self,nums,value):
        if not nums:
            return False
        n = len(nums)
        l,r = 0,n - 1
        if n == 1:
            return nums[0] == value
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] == value:
                return True
            elif nums[l] == nums[mid] and nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]:
                if nums[l] <= value and value < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < value <= nums[n - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
