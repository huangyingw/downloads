class Solution(object):
    def minimumTotal(self, triangle):
        dp = [0] * (len(triangle) + 1)
        for row in range(len(triangle) - 1, -1, -1):
            for col in range(row):
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
        return dp[0]

