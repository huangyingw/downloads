class Solution(object):
    def gameOfLife(self, board):
        if not board or len(board) == 0 or len(board[0]) == 0:
            return
        for i in range(len(board)):
            for j in range(len(board[0])):
                lives = self.findLives(board, i, j)
                if board[i][j] == 1 and (lives < 2 or lives > 3):
                    board[i][j] = 3
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 1 if board[i][j] in [1, 2] else 0

    def findLives(self, board, i, j):
        lives = 0
        for row_offset in range(-1, 2):
            for col_offset in range(-1, 2):
                if row_offset == col_offset == 0:
                    continue
                if 0 <= i + row_offset < len(board) and 0 <= j + col_offset < len(board[0]):
                lives += 1 if board[i + row_offset][j + col_offset] in [1, 3] else 0
        return lives

