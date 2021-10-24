class Solution:
    def sort_color(self,numbers):
        if not numbers:
            return []
        n = len(numbers)
        p0,p1 = 0,n - 1
        i = 0
        while i <= p1:
            while i <= p1 and numbers[i] == 2:
                numbers[i],numbers[p1] = numbers[p1],numbers[i]
                p1 -= 1
            if numbers[i] == 0:
                numbers[i],numbers[p0] = numbers[p0],numbers[i]
                p0 += 1
            i += 1
        return numbers

result = Solution()
numbers = [0]
print(result.sort_color(numbers))
