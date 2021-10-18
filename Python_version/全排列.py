class Solution:
    def full(self,nums):
        def back_track(first = 0):
            if first == n:
                ans.append(nums[:])
                return
            for i in range(first,n):
                nums[first],nums[i] = nums[i],nums[first]
                back_track(first + 1)
                nums[first],nums[i] = nums[i],nums[first]
        ans = []
        n = len(nums)
        back_track()
        return ans

result = Solution()
print(result.full([1]))
