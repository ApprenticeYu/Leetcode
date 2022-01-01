class Solution:
    def __init__(self,nums):
        self.nums = nums
        self.origin = nums.copy()

    def reset(self):
        self.nums = self.origin.copy()
        return self.nums

    def shuffle_array(self):
        for i in range(len(self.nums)):
            j = random.randrange(i,len(self.nums))
            self.nums[i],self.nums[j] = self.nums[j],self.nums[i]
        return self.nums
