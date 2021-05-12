class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True

    def search(self, word):
        node = self.root
        return self.helper(word, node)

    def helper(self, word, node):
        if len(word) == 0:
            return node.isWord
        curr = word[0]
        if curr == '.':
            for k in node.children:
                if self.helper(word[1:], node.children[k]):
                    return True
        else:
            if curr not in node.children:
                return False
            return self.helper(word[1:], node.children[curr])
        return False

