class Solution:
    def search(self,nums,target):
        if not nums:
            return -1
        left,right = 0,len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[0] <= nums[middle]:
                if nums[0] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[middle] < target <= nums[len(nums) - 1]:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1
result = Solution()
print(result.search([1],0))
