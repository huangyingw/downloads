class Solution(object):
    def indexPairs(self, text, words):
        result = []
        for word in words:
            idx = -1
            while True:
                idx = text.find(word, idx + 1)
                if idx == -1:
                    break
                result.append([idx, idx + len(word) - 1])
        return sorted(result)

