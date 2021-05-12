class Solution(object):
    def numDistinct(self, s, t):
        dp = [0 for _ in range(len(t) + 1)]
        dp[0] = 1

        for i in range(1, len(s) + 1):
            for j in range(len(t), 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[len(t)]

