class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        maxLen = 0
        dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        for row in range(1, len(matrix) + 1):
            for col in range(1, len(matrix[0]) + 1):
                if matrix[row - 1][col - 1] == '1':
                    dp[row][col] = min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1]) + 1
                else:
                    dp[row][col] = 0
                maxLen = max(maxLen, dp[row][col])
        return maxLen * maxLen

