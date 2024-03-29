class Solution(object):
    def exist(self, board, word):
        result = False
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.dfs(board, word, row, col, 0):
                    return True
        return False

    def dfs(self, board, word, row, col, curr_len):
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return False
        if board[row][col] == word[curr_len]:
            if curr_len == len(word) - 1:
                return True
            c = board[row][col]
            board[row][col] = '#'
            if (self.dfs(board, word, row - 1, col, curr_len + 1) or self.dfs(board, word, row + 1, col, curr_len + 1) or self.dfs(board, word, row, col - 1, curr_len + 1) or self.dfs(board, word, row, col + 1, curr_len + 1)):
                return True
            board[row][col] = c
        return False

