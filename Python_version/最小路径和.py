class Solution:
    def min_path_sum(self,matrix):
        if not matrix or not matrix[0]:
            return 0
        m,n = len(matrix),len(matrix[0])
        length = [0] * n
        length[0] = matrix[0][0]
        for i in range(1,n):
            length[i] = length[i - 1] + matrix[0][i]
        for i in range(1,m):
            for j in range(n):
                if j == 0:
                    length[j] += matrix[i][0]
                else:
                    length[j] = min(length[j],length[j - 1]) + matrix[i][j]
        return length[n - 1]

result = Solution()
matrix = [[1,2,3],[4,5,6]]
print(result.min_path_sum(matrix))
