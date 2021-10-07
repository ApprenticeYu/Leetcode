class Solution:
    def remove_duplicate_numbers(self,numbers):
        if not numbers:
            return 0
        n = len(numbers)
        slow,fast = 1,1
        while fast < n:
            if numbers[fast] != numbers[fast - 1]:
                numbers[slow] = numbers[fast]
                slow += 1
            fast += 1
        return slow

result = Solution()
print(result.remove_duplicate_numbers([0,0,1,1,1,2,2,3,3,4]))
