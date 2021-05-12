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
        queue, visited = [], set()
        queue.append((beginWord, 1))
        while queue:
            word, steps = queue.pop(0)
            visited.add(word)
            if word == endWord:
                return steps
            for index in range(len(word)):
                s = word[:index] + "_" + word[index + 1:]
                for neigh in d.get(s, []):
                    if neigh not in visited:
                        queue.append((neigh, steps + 1))
        return 0

