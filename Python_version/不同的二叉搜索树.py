class Solution:
    def different_tree(self,n):
        C = 1
        for i in range(0,n):
            C = C * (2 * (2 * i + 1) / (i + 2))
        return int(C)
