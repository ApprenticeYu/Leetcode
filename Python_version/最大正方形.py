class Solution:
    def max_matrix(self,matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        maxside = 0
        rows = len(matrix)
        columns = len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j],dp[i][j - 1],dp[i - 1][j - 1]) + 1
                    maxside = max(maxside,dp[i][j])
        max_area = maxside * maxside
        return max_area
