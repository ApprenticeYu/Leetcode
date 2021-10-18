class Solution:
    def matrix_0(self,matrix):
        if not matrix or not matrix[0]:
            return []
        m,n = len(matrix),len(matrix[0])
        flag_0 = False
        for i in range(m):
            if matrix[i][0] == 0:
                flag_0 = True
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(m - 1,-1,-1):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if flag_0:
                matrix[i][0] = 0
        return matrix

result = Solution()
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(result.matrix_0(matrix))
