class Solution:
    def jump(self,nums):
        n,rightmost = len(nums),0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(i + nums[i],rightmost)
            if rightmost >= n - 1:
                return True
        return False

result = Solution()
print(result.jump([3,2,1,0,4]))
