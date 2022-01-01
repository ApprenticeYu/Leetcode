class Solution:
    def miss_game(self,n):
        return 1 if n == 1 else 2*(n // 2 + 1 - self.miss_game(n // 2))
