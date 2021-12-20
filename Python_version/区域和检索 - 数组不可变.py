class Solution:
    def __init__(self,nums):
        self.d = [0]
        _d = self.d

        for num in nums:
            _d.append(_d[-1] + num)

    def area_find(self,i,j):
        _d = self.d
        return _d[j + 1] - _d[i]
