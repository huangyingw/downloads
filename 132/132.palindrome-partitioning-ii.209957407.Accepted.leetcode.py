class Solution(object):
    def minCut(self, s):
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        isPalin = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(0, n + 1):
            dp[i] = n - 1 - i

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or isPalin[i + 1][j - 1]):
                    isPalin[i][j] = True
                    dp[i] = min(dp[i], dp[j + 1] + 1)

        return dp[0]

