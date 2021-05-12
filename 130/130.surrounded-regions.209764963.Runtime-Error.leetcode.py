class Solution(object):
    class Pos:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    def isOutOfBound(self, x, y, rows, columns):
        return x < 0 or y < 0 or x >= rows or y >= columns

    def solve(self, board):
        if not board or not board[0]:
            return

        rows = len(board)
        columns = len(board[0])
        queue = []

        for i in range(0, rows):
            queue.append(self.Pos(i, 0))
            queue.append(self.Pos(i, columns - 1))

        for i in range(0, columns):
            queue.append(self.Pos(0, i))
            queue.append(self.Pos(rows - 1, i))

        while not queue.isEmpty():
            pos = queue.remove()

            if self.isOutOfBound(pos.x, pos.y, rows, columns) or board[pos.x][pos.y] != 'O':
                continue

            board[pos.x][pos.y] = 'N'
            queue.append(self.Pos(pos.x - 1, pos.y))
            queue.append(self.Pos(pos.x + 1, pos.y))
            queue.append(self.Pos(pos.x, pos.y - 1))
            queue.append(self.Pos(pos.x, pos.y + 1))

        for i in range(0, rows):
            for j in range(0, columns):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'N':
                    board[i][j] = 'O'

