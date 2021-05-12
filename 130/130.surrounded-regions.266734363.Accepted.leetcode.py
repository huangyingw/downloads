class Solution(object):
    def solve(self, board):
        if len(board) == 0:
            return
        for row in range(len(board)):
            if board[row][0] == 'O':
                self.merge(board, row, 0)
            if board[row][len(board[0]) - 1] == 'O':
                self.merge(board, row, len(board[0]) - 1)
        for col in range(len(board[0])):
            if board[0][col] == 'O':
                self.merge(board, 0, col)
            if board[len(board) - 1][col] == 'O':
                self.merge(board, len(board) - 1, col)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == '#':
                    board[row][col] = 'O'

    def merge(self, board, row, col):
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return
        if board[row][col] != 'O':
            return
        board[row][col] = '#'
        self.merge(board, row + 1, col)
        self.merge(board, row, col - 1)
        self.merge(board, row, col + 1)
        self.merge(board, row - 1, col)

