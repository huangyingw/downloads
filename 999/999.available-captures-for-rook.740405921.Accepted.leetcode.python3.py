class Solution(object):
    def numRookCaptures(self, board):
        result = 0
        rook_index = (0, 0)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'R':
                    rook_index = (row, col)
                    break
        flag = True
        col = rook_index[1] - 1
        pawn = 0
        while col >= 0:
            if board[rook_index[0]][col] == 'B':
                flag = False
                break
            if board[rook_index[0]][col] == 'p':
                pawn += 1
                break
            col -= 1
        if flag and pawn != 0:
            result += 1
        flag = True
        col = rook_index[1] + 1
        pawn = 0
        while col < len(board[0]):
            if board[rook_index[0]][col] == 'B':
                flag = False
                break
            if board[rook_index[0]][col] == 'p':
                pawn += 1
                break
            col += 1
        if flag and pawn != 0:
            result += 1
        flag = True
        row = rook_index[0] + 1
        pawn = 0
        while row < len(board):
            if board[row][rook_index[1]] == 'B':
                flag = False
                break
            if board[row][rook_index[1]] == 'p':
                pawn += 1
                break
            row += 1
        if flag and pawn != 0:
            result += 1
        pawn = 0
        flag = True
        row = rook_index[0] - 1
        while row >= 0:
            if board[row][rook_index[1]] == 'B':
                flag = False
                break
            if board[row][rook_index[1]] == 'p':
                pawn += 1
                break
            row -= 1
        if flag and pawn != 0:
            result += 1
        return result

