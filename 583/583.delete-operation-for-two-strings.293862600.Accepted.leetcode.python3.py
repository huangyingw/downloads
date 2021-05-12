class Solution:
    def minDistance(self, word1, word2):
        L1, L2 = len(word1), len(word2)
        d = [[0] * (L2 + 1) for _ in range(L1 + 1)]
        for i, l1 in enumerate(word1):
            for j, l2 in enumerate(word2):
                if l1 == l2:
                    d[i][j] = d[i - 1][j - 1] + 1
                else:
                    d[i][j] = max(d[i - 1][j], d[i][j - 1])
        len_lcs = d[L1 - 1][L2 - 1]
        return L1 + L2 - 2 * len_lcs

