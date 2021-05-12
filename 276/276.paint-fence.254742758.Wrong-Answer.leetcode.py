class Solution(object):
    def numWays(self, n, k):
        dp = [0, k, k * k]
        if n <= 2:
            return dp[n]
        dp[0] = k
        dp[1] = k * k
        for idx in range(2, n):
            dp[0], dp[1], dp[2] = dp[1], dp[2], (k - 1) * (dp[0] + dp[1])
            print('dp[0] --> %s' % (dp[0]))
            print('dp[1] --> %s' % (dp[1]))
            print('dp[2] --> %s' % (dp[2]))
        return dp[2]

