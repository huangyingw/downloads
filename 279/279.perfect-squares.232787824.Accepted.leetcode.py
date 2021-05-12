class Solution(object):
    def numSquares(self, n):
        dp = collections.defaultdict(int)
        y = 1
        while y * y <= n:
            dp[y * y] = 1
            y += 1
        for x in range(1, n + 1):
            y = 1
            while x + y * y <= n:
                if x + y * y not in dp or dp[x] + 1 < dp[x + y * y]:
                    dp[x + y * y] = dp[x] + 1
                y += 1
        return dp[n]

