class Solution:
    def num_replace(self,n):
        ret = 0
        while n != 1:
            if n % 2 == 0:
                ret += 1
                n //= 2
            elif n % 4 == 1:
                ret += 2
                n //= 2
            else:
                if n == 3:
                    ret += 2
                    n = 1
                else:
                    ret += 2
                    n = n // 2 + 1
        return ret
