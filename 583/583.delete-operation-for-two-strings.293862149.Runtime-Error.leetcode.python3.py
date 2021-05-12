class Solution:
    def minDistance(self, word1, word2):
        return len(word1) + len(word2) - 2 * self.lcs(word1, word2, len(word1), len(word2))

    def lcs(self, s1, s2, m, n):
        if m == 0 and n == 0:
            return 0
        if (s1[m - 1] == s2[n - 1]):
            return 1 + self.lcs(s1, s2, m - 1, n - 1)
        else:
            return max(self.lcs(s1, s2, m, n - 1), self.lcs(s1, s2, m - 1, n))

