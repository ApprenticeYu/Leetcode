class Solution:
    def guess_number(self,n):
        left,right = 1,n
        while left < right:
            mid = (left + right) // 2
            if guess(mid) <= 0:
                right = mid
            else:
                left = mid + 1
            return left
