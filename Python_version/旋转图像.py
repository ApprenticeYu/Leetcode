class Solution:
    def rotate_matrix(self,matrix):
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j],matrix[n - j - 1][i],matrix[n - i - 1][n - j - 1],matrix[j][n - i - 1] = matrix[n - j - 1][i],matrix[n - i - 1][n - j - 1],matrix[j][n - i - 1],matrix[i][j]

result = Solution()
matrix = [[1,2],[3,4]]
result.rotate_matrix(matrix)
print(matrix)
