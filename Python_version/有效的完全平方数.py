class Solution:
    def valid_num(self,num):
        left,right = 0,num
        while left <= right:
            mid = (left + right) // 2
            squar = mid * mid
            if squar < num:
                left = mid + 1
            elif squar > num:
                right = mid - 1
            else:
                return True
        return False
