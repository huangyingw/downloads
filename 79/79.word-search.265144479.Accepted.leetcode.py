class Solution1:
    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]
        board[i][j] = "#"
        res = self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i - 1, j, word[1:]) \
            or self.dfs(board, i, j + 1, word[1:]) or self.dfs(board, i, j - 1, word[1:])
        board[i][j] = tmp
        return res
from collections import Counter


class Solution:
    def exist(self, board, word):
        if not board or not board[0] or not word:
            return False
        if not self.checkContent(board, word):
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j] and \
                        self.deepDive(board, i, j, word, 1):
                    return True
        return False

    def checkContent(self, board, word):
        board_counter = Counter([char for row in board for char in row])
        word_counter = Counter(word)
        for char in word_counter:
            if board_counter[char] < word_counter[char]:
                return False
        return True

    def deepDive(self, board, i, j, word, position):
        if len(word) == position:
            return True
        m, n = len(board), len(board[0])
        old, board[i][j] = board[i][j], '#'
        if i > 0 and board[i - 1][j] != '#' and board[i - 1][j] == word[position] and \
                self.deepDive(board, i - 1, j, word, position + 1):
            return True
        if i + 1 < m and board[i + 1][j] != '#' and board[i + 1][j] == word[position] and \
                self.deepDive(board, i + 1, j, word, position + 1):
            return True
        if j > 0 and board[i][j - 1] != '#' and board[i][j - 1] == word[position] and \
                self.deepDive(board, i, j - 1, word, position + 1):
            return True
        if j + 1 < n and board[i][j + 1] != '#' and board[i][j + 1] == word[position] and \
                self.deepDive(board, i, j + 1, word, position + 1):
            return True
        board[i][j] = old
        return False

