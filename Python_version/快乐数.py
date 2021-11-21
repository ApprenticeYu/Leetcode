class Solution:
    def is_happy(self,n):
        def get_next(num):
            total_sum = 0
            while num > 0:
                num,result = divmod(num,10)
                total_sum += result ** 2
            return total_sum

        slow = n
        fast = get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1
