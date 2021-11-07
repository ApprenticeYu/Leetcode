class Solution:
    def min_path_sum(self,nums):
        n = len(nums)
        f = [0] * n
        f[0] = nums[0][0]
        for i in range(1,n):
            f[i] = f[i - 1] + nums[i][i]
            for j in range(i - 1,0,-1):
                f[j] = min(f[j],f[j - 1]) + nums[i][j]
            f[0] += nums[i][0]
        return min(f)
