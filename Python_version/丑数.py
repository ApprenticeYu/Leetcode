class Solution:
    def ugly_number(self,num):
        if num <= 0:
            return False
        factor = [2,3,5]
        for i in factor:
            while num % i == 0:
                num //= i
        return num == 1
