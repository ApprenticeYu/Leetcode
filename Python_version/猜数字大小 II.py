class Solution:
    def guess_number(self,n):
        f = [0] * (n + 1) for _ in range(n + 1)
        for i in range(n - 1,0,-1):
            for j in range(i + 1,n + 1):
                f[i][j] = j + f[i][j - 1]

                for k in range(i,j):
                    f[i][j] = min(f[i][j],max(k + f[i][k - 1],k + f[k + 1][j]))
        return f[1][n]
