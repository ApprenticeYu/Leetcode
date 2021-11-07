class Solution:
    def only_once(self,nums):
        return reduce(lambda x,y:x ^ y,nums)
