class Solution(object):
    def numDistinct(self, s, t):
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = 1

        for i in range(1, len(s) + 1):
            dp[i][0] = 1

            for j in range(len(t), 0, -1):
                dp[i][j] = dp[i - 1][j]

                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[len(s)][len(t)]

