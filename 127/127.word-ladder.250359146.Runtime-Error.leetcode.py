class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordDict = set(wordList)
        if endWord not in wordDict:
            return 0
        l = len(beginWord)
        beginWord = {beginWord}
        endWord = {endWord}
        wordDict.remove(endWord)
        step = 0
        while len(beginWord) > 0 and len(endWord) > 0:
            step += 1
            if len(beginWord) > len(endWord):
                beginWord, endWord = endWord, beginWord
            s = set()
            for w in beginWord:
                new_words = [w[:i] + t + w[i + 1:] for t in string.ascii_lowercase for i in xrange(l)]
                for new_word in new_words:
                    if new_word in endWord:
                        return step + 1
                    if new_word not in wordDict:
                        continue
                    wordDict.remove(new_word)
                    s.add(new_word)
            beginWord = s
        return 0

