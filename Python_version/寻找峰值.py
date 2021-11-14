class Solution:
    def find_top(self,nums):
        n = len(nums)
        def get(i):
            if i == -1 or i == n:
                return float("-inf")
            return nums[i]
        left,right,ans = 0,n - 1,-1
        while left <= right:
            mid = (left + right) // 2
            if get(mid - 1) < get(mid) > get(mid + 1):
                ans = mid
                break
            elif get(mid) < get(mid + 1):
                left = mid + 1
            elif get(mid) > get(mid + 1):
                right = mid - 1
        return ans
