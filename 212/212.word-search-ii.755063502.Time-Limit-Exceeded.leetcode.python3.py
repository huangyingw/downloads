class Node:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution(object):
    def findWords(self, board, words):
        root = Node()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = Node()
                node = node.children[c]
            node.word = word
        found = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.search(board, root, r, c, found)
        return found

    def search(self, board, node, r, c, found):
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
            return
        letter = board[r][c]
        if letter not in node.children:
            return
        node = node.children[letter]
        if node.word:
            found.append(node.word)
            node.word = None
        board[r][c] = '*'
        self.search(board, node, r + 1, c, found)
        self.search(board, node, r - 1, c, found)
        self.search(board, node, r, c + 1, found)
        self.search(board, node, r, c - 1, found)
        board[r][c] = letter

