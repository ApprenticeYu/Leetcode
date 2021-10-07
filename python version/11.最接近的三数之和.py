class Solution:
    def thenearestsum(self,numbers,target):
        n = len(numbers)
        numbers.sort()
        optim = 10 ** 7

        def update(number):
            nonlocal optim
            if abs(number - target) < abs(optim - target):
                optim = number

        for i in range(n):
            j,end = i + 1,n - 1
            while j < end:
                sumofthree = numbers[i] + numbers[j] + numbers[end]
                update(sumofthree)
                if sumofthree == target:
                    return target
                elif sumofthree > target:
                    end_temp = end - 1
                    while j < end_temp and numbers[end_temp] == numbers[end_temp + 1]:
                        end_temp -= 1
                    end = end_temp
                else:
                    j_temp = j + 1
                    while j_temp < end and numbers[j_temp] == numbers[j_temp - 1]:
                        j_temp += 1
                    j = j_temp
        return optim

result = Solution()
print(result.thenearestsum([-1,2,1,-4],1))
