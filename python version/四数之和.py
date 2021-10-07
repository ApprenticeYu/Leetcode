class Solution:
    def sumoffour(self,numbers,target):
        ans = list()
        n = len(numbers)
        if not numbers or n < 4:
            return ans
        numbers.sort()
        for i in range(n - 3):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            if numbers[i] + numbers[i + 1] + numbers[i + 2] + numbers[i + 3] > target:
                break
            if numbers[i] + numbers[n - 1] + numbers[n - 2] + numbers[n - 3] < target:
                continue
            for j in range(i + 1,n - 2):
                if j > i + 1 and numbers[j] == numbers[j - 1]:
                    continue
                if numbers[i] + numbers[j] + numbers[j + 1] + numbers[j + 2] > target:
                    break
                if numbers[i] + numbers[j] + numbers[n - 1] + numbers[n - 2] < target:
                    continue
                left,right = j + 1,n - 1
                while left < right:
                    sum = numbers[i] + numbers[j] + numbers[left] + numbers[right]
                    if sum == target:
                        ans.append([numbers[i],numbers[j],numbers[left],numbers[right]])
                        while left < right and numbers[left] == numbers[left + 1]:
                            left += 1
                        left += 1
                        while left < right and numbers[right] == numbers[right - 1]:
                            right -= 1
                        right -= 1
                    elif sum < target:
                        left += 1
                    else:
                        right -= 1
        return ans

result = Solution()
print(result.sumoffour([2,2,2,2,2],8))
