class WordDictionary(object):
    class TrieNode(object):
        def __init__(self, content=' '):
            self.content = content
            self.isWord = False
            self.nexts = {}

    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word):
        current = self.root

        for i in range(0, len(word)):
            c = word[i]
            print("current.nexts --> %s" % str(current.nexts))
            node = current.nexts[c]

            if not node:
                current.nexts[c] = self.TrieNode(c)
                node = current.nexts[c]
            current = node
        current.isWord = True

    def search(self, word):
        if not word:
            return False

        trieNode = self.root
        return self.dfs(word, 0, trieNode)

    def dfs(self, word, index, trieNode):
        if index == len(word) - 1:
            if word[index] == '.':
                for _, tNode in trieNode.nexts:
                    if tNode.isWord:
                        return True
                return False
            else:
                endNode = trieNode.nexts.get(word[index])
                return endNode and endNode.isWord

        if index >= len(word):
            return False

        if word[index] == '.':
            for _, node in trieNode.nexts:
                if self.dfs(word, index + 1, node):
                    return True
            return False
        else:
            if word[index] in trieNode.nexts:
                return self.dfs(word, index + 1, trieNode.nexts[word[index]])
            else:
                return False

