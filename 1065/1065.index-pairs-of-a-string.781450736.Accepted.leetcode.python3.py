class Solution(object):
    def indexPairs(self, text, words):
        if not words:
            return []
        result = []
        for word in words:
            starting = [index for index in range(len(text)) if text.startswith(word, index)]
            for start in starting:
                result.append([start, start + len(word) - 1])
        result.sort()
        return result

