class Solution:
    def minDistance(self, word1, word2):
        def lcs(s1, s2, m, n, memo):
            if m == 0 and n == 0:
                return 0
            if memo[m][n] > 0:
                return memo[m][n]
            if (s1[m - 1] == s2[n - 1]):
                memo[m][n] = 1 + self.lcs(s1, s2, m - 1, n - 1, memo)
            else:
                memo[m][n] = max(lcs(s1, s2, m, n - 1), lcs(s1, s2, m - 1, n), memo)
            return memo[m][n]
        memo = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
        return len(word1) + len(word2) - 2 * lcs(word1, word2, len(word1), len(word2), memo)

