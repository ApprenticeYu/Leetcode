class Solution:
    def add_1(self,numbers):
        n = len(numbers)
        for i in range(n - 1,-1,-1):
            numbers[i] += 1
            numbers[i] %= 10
            if numbers[i] != 0:
                return numbers
        numbers = [0] * (n + 1)
        numbers[0] = 1
        return numbers

result = Solution()
numbers = [0]
print(result.add_1(numbers))
