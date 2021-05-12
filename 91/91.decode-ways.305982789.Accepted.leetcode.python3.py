class Solution:
    def numDecodings(self, s):
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        if 0 < int(s[0]) <= 26:
            dp[1] = 1
        for i in range(1, n):
            if 0 < int(s[i]) <= 26:
                dp[i + 1] += dp[i]
            if 0 < int(s[i - 1:i + 1]) <= 26 and s[i - 1:i + 1][0] != '0':
                dp[i + 1] += dp[i - 1]
        return dp[n]

