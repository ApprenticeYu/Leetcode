class Solution:
    def reverse(self,num):
        MIN_NUM,MAX_NUM = -2**31,2**31 - 1
        ret = 0
        while(num):
            if num < MIN_NUM // 10 + 1 or num > MAX_NUM // 10:
                return 0
            digit = num % 10
            if num < 0 and digit > 0:
                digit -= 10
            num = (num - digit) // 10
            ret = ret * 10 + digit
        return ret
result = Solution()
print(result.reverse(0))
