class Solution(object):
    def minimumTotal(self, triangle):
        dp = [0 for _ in range(len(triangle))]
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
        return dp[0]

