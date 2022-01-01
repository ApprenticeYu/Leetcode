class Solution:
    def nth_bit(self,num):
        d,count = 1,9
        while n > d * count:
            n -= d * count
            d += 1
            count *= 10
        index = n - 1
        start = 10 ** (d - 1)
        num = start + index // d
        digit_index = index % d
        return num // 10 ** (d - digit_index - 1) % 10
