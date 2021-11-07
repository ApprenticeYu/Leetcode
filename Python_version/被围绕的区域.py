class Solution:
    def surround_area(self,board):
        if not board:
            return
        m = len(board)
        n = len(board[0])
        def dfs(l,r):
            if not 0 <= l < m or not 0 <= r < n or board[l][r] != '0':
                return
            board[l][r] = 'A'
            dfs(l + 1,r)
            dfs(l - 1,r)
            dfs(l,r + 1)
            dfs(l,r - 1)
        for i in range(m):
            dfs(i,0)
            dfs(i,n - 1)
        for j in range(m - 1):
            dfs(0,j)
            dfs(m - 1,j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'A':
                    board[i][j] = '0'
                elif board[i][j] == '0':
                    board[i][j] = 'X'
                
