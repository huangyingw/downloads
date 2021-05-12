class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.is_leaf = True

    def search(self, word):
        return self.helper(word, self.root)

    def helper(self, word, node):
        if len(word) == 0:
            return node.is_leaf
        first = word[0]
        if first == ".":
            for key in node.children:
                if self.helper(word[1:], node.children[key]):
                    return True
        else:
            if first not in node.children:
                return False
            return self.helper(word[1:], node.children[first])
        return False

