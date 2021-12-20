class Solution:
    def __init__(self,matrix):
        m,n = len(matrix),(len(matrix[0]) if matrix else 0)
        self.sum = [[0] * (n + 1) for _ in range(m + 1)]
        _sum = self.sum
        for r in range(m):
            for c in range(n):
                _sum[r + 1][c + 1] = _sum[r][c + 1] + _sum[r + 1][c] - _sum[r][c] + matrix[r][c]
    def fix_matrix(self,r1,c1,r2,c2):
        _sum = self.sum
        return _sum[r2 + 1][c2 + 1] - _sum[r1][c2 + 1] - _sum[r2 + 1][c1] + _sum[r1][c1]
