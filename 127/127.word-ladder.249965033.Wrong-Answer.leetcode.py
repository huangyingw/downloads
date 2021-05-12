class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if not wordList:
            return 0
        queue = [beginWord]
        distance = 1
        while queue:
            currWord = queue.pop(0)
            if currWord == endWord:
                return distance
            for i in range(len(beginWord)):
                alphabets = string.ascii_lowercase
                for c in alphabets:
                    newWord = currWord[:i] + c + currWord[i + 1:]
                    if newWord in wordList:
                        queue.append(newWord)
                        distance += 1
                        wordList.remove(newWord)
        return 0

