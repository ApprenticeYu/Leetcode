class Solution:
    def different_path(self,m,n):
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1,m):
            for j in range(1,n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]

result = Solution()
print(result.different_path(3,3))
