class Solution(object):
    def palindromePairs(self, words):
        word2index, res = dict([(w[::-1], i) for i, w in enumerate(words)]), []
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix, postfix = word[:j], word[j:]
                if prefix in word2index and i != word2index[prefix] and postfix == postfix[::-1]:
                    res.append([i, word2index[prefix]])
                if j > 0 and postfix in word2index and i != word2index[postfix] and prefix == prefix[::-1]:
                    res.append([word2index[postfix], i])
        return res

