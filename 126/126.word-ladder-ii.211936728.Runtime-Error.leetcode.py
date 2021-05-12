class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        def buildPath(path, word):
            if len(preMap[word]) == 0:
                result.append([word] + path)
                return
            path.insert(0, word)
            for w in preMap[word]:
                buildPath(path, w)
            path.pop(0)

        length = len(beginWord)
        preMap = {}
        for word in wordlist:
            preMap[word] = []
        result = []
        cur_level = set()
        cur_level.add(beginWord)

        while True:
            pre_level = cur_level
            cur_level = set()
            for word in pre_level:
                wordlist.remove(word)
            for word in pre_level:
                for i in range(length):
                    left = word[:i]
                    right = word[i + 1:]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c != word[i]:
                            nextWord = left + c + right
                            if nextWord in wordlist:
                                preMap[nextWord].append(word)
                                cur_level.add(nextWord)
            if len(cur_level) == 0:
                return []
            if endWord in cur_level:
                break
        buildPath([], endWord)
        return result

