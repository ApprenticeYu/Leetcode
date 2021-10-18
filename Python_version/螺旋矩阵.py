class Solution:
    def rotate_matrix(self,matrix):
        if not matrix or not matrix[0]:
            return list()
        rows,columns = len(matrix),len(matrix[0])
        top,bottom,left,right = 0,rows - 1,0,columns - 1
        ans = list()
        while left <= right and top <= bottom:
            for column in range(left,right + 1):
                ans.append(matrix[top][column])
            for row in range(top + 1,bottom + 1):
                ans.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1,left,-1):
                    ans.append(matrix[bottom][column])
                for row in range(bottom,top,-1):
                    ans.append(matrix[row][left])
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return ans

result = Solution()
print(result.rotate_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
