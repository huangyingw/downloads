class Solution:
    def minPathSum(self, grid):
        if not grid:
            return None
        n = len(grid[0])
        m = len(grid)
        dp = [0 for _ in range(n)]
        dp[0] = grid[0][0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + grid[0][i]
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
        return dp[-1]

