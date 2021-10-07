class Solution:
    def maxarea(self,numbers):
        n = len(numbers)
        left,right = 0,n - 1
        ans = 0
        while left < right:
            area = min(numbers[left],numbers[right]) * (right - left)
            ans = max(ans,area)
            if numbers[left] < numbers[right]:
                left += 1
            else:
                right -= 1
        return ans

result = Solution()
print(result.maxarea([1,2,1])) 
