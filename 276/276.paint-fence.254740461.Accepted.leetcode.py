class Solution(object):
    def numWays(self, n, k):
        if n == 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k * k
        dp = [0] * n
        dp[0] = k
        dp[1] = k * k
        for idx in range(2, n):
            dp[idx] = (k - 1) * (dp[idx - 1] + dp[idx - 2])
        return dp[n - 1]

