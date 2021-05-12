class Solution:
    def minimumTotal(self, triangle):
        dp = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for j in range(len(row)):
                dp[j] = min(dp[j], dp[j + 1]) + row[j]
        return dp[0]

