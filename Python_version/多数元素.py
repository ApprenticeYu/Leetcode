class Solution:
    def amount_numbers(self,numbers):
        times = 0
        candidate = None
        for number in numbers:
            if times == 0:
                candidate = number
            times += (1 if candidate == number else -1)
        return candidate
