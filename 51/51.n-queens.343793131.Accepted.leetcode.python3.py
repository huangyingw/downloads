class Solution:
    def solveNQueens(self, n):
        def dfs(row):
            if row == n:
                ret.append([''.join(r) for r in chessboard])
                return
            for col in range(n):
                if isValid(row, col):
                    chessboard[row][col] = 'Q'
                    dfs(row + 1)
                    chessboard[row][col] = '.'

        def isValid(row, col):
            for i in range(row):
                for j in range(n):
                    if chessboard[i][j] == 'Q' and (col == j or row - col == i - j or row + col == i + j):
                        return False
            return True
        chessboard = [['.'] * n for i in range(n)]
        ret = []
        dfs(0)
        return ret

