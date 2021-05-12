class Solution():
    def ladderLength(self, beginWord, endWord, wordList):
        d = {}
        for word in wordList:
            for i in range(len(word)):
                s = word[:i] + "_" + word[i + 1:]
                if s in d:
                    d[s].append(word)
                else:
                    d[s] = [word]
        print d
        queue, visited = [], set()
        queue.append((beginWord, 1))
        while queue:
            word, steps = queue.pop(0)
            if word not in visited:
                visited.add(word)
                if word == endWord:
                    return steps
                else:
                    for index in range(len(word)):
                        s = word[:index] + "_" + word[index + 1:]
                        neigh_words = []
                        if s in d:
                            neigh_words = d[s]
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
        return 0

