class Solution:
    def zero(self,n):
        zero_number = 0
        while n > 0:
            n //= 5
            zero_number += n
        return zero_number
