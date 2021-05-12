class Solution(object):
    def numWays(self, n, k):
        dp = [0, k, k * k]
        if n <= 2:
            return dp[n]
        for idx in range(2, n):
            dp[2], dp[0], dp[1] = (k - 1) * (dp[0] + dp[1]), dp[1], dp[2]
        return dp[2]

