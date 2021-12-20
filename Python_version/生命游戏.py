class Solution:
    def live_game(self,board):
        rows = len(board)
        columns = len(board[0])
        neighbors = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,1),(1,-1),(-1,1)]
        for r in rows:
            for c in columns:
                live_num = 0
                for neighbor in neighbors:
                    r_temp = r + neighbor[0]
                    c_temp = c + neighbor[1]
                    if r_temp >= 0 and r_temp < r and c_temp >= 0 and c_temp < c and board[r_temp,c_temp] == 1:
                        live_num += 1
                if board[r][c] == 1 and (live_num < 2 or live_num > 3):
                    board[r][c] = -1
                if board[r][c] == 0 and live_num == 3:
                    board[r][c] = 2

         for r in rows:
             for c in columns:
                 if board[r][c] > 0:
                     board[r][c] = 1
                 if board[r][c] < 0:
                     board[r][c] = 0
