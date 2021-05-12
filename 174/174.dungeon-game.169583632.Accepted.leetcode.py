class Solution(object):
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [sys.maxint] * (n + 1)
        dp[n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[j] = max(1, min(dp[j], dp[j + 1]) - dungeon[i][j])

        return dp[0]

