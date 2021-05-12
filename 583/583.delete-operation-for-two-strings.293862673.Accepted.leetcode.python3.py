class Solution:
    def minDistance(self, word1, word2):
        if len(word1) == 0 or len(word2) == 0:
            return len(word1) + len(word2)
        a = [0] * len(word1)
        b = [0] * len(word1)
        for i in range(len(word2)):
            b[0] = 1 if word2[i] == word1[0] else a[0]
            for j in range(1, len(word1)):
                b[j] = a[j - 1] + 1 if word2[i] == word1[j] else max(b[j - 1], a[j])
            a, b = b, a
        return len(word1) + len(word2) - 2 * max(a[-1], b[-1])

