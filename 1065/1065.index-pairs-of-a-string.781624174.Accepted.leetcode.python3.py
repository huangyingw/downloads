class Solution(object):
    def indexPairs(self, text, words):
        result = []
        for word in words:
            starting = [[index, index + len(word) - 1] for index in range(len(text)) if text.startswith(word, index)]
            result += starting
        result.sort()
        return result

