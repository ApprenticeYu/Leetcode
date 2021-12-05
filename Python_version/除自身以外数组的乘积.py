class Solution:
    def product_except_self(self,nums):
        n = len(nums)
        answers = [0] * n
        answers[0] = 1
        for i in range(1,n):
            answers[i] = nums[i - 1] * answers[i - 1]
        R = 1
        for i in reversed(range(n)):
            answers[i] = answers[i] * R
            R *= nums[i]
        return answers
