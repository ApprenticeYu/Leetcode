class Solution:
    def threesum(self,numbers):
        n = len(numbers)
        numbers.sort()
        ans = list()
        for i in range(n):
            if i != 0 and numbers[i] == numbers[i - 1]:
                continue
            target = -numbers[i]
            end = n - 1
            for j in range(i + 1,n):
                if j > i + 1 and numbers[j] == numbers[j - 1]:
                    continue
                while j < end and numbers[j] + numbers[end] > target:
                    end -= 1
                if j == end:
                    break
                if numbers[j] + numbers[end] == target:
                    ans.append([numbers[i],numbers[j],numbers[end]])
        return ans

result = Solution()
print(result.threesum([-1,0,1,2,-1,-4]))
