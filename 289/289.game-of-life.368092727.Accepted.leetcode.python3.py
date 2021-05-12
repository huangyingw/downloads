class Solution(object):
    def gameOfLife(self, board):

        def count(x, y):
            res = 0
            for r in range(x - 1, x + 2):
                for c in range(y - 1, y + 2):
                    if (r != x or c != y) and 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] > 0:
                        res += 1
            return res
        for x in range(len(board)):
            for y in range(len(board[0])):
                board[x][y] = count(x, y) + 1 if board[x][y] == 1 else - count(x, y)
        for x in range(len(board)):
            for y in range(len(board[0])):
                board[x][y] = 1 if board[x][y] in {3, 4, -3} else 0

