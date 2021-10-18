class Solution:
    def rotate_matrix_2(self,n):
        matrix = [[0] * n for _ in range(n)]
        top,left,right,bottom = 0,0,n - 1,n - 1
        num = 1
        while left <= right and top <= bottom:
            for column in range(left,right + 1):
                matrix[top][column] = num
                num += 1
            for row in range(top + 1,bottom + 1):
                matrix[row][right] = num
                num += 1
            if top < bottom and left < right:
                for column in range(right - 1,left,-1):
                    matrix[bottom][column] = num
                    num += 1
                for row in range(bottom,top,-1):
                    matrix[row][left] = num
                    num += 1
            top,left,right,bottom = top + 1,left + 1,right - 1,bottom - 1
        return matrix

result = Solution()
print(result.rotate_matrix_2(1))
