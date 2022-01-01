class Solution:
    def Kth_number(self,matrix,k):
        n = len(matrix)

        def check(mid):
            i,j = n - 1,0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num <= k

        left,right = matrix[0][0],matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left
