class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix:
            return 0

        maxLen = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for x in range(m + 1)]

        for row in range(1, len(matrix) + 1):
            for col in range(1, len(matrix[0]) + 1):
                if matrix[row - 1][col - 1] == '1':
                    minDP = min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1])
                    dp[row][col] = minDP + 1
                else:
                    dp[row][col] = 0
                maxLen = max(maxLen, dp[row][col])

        return maxLen * maxLen

