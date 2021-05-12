class Solution(object):
    def maximalSquare(self, matrix):
        if matrix is None or len(matrix) == 0:
            return 0
        rows, cols, maxLen, prev = len(matrix), len(matrix[0]), 0, 0
        dp = [0] * (cols + 1)
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                temp = dp[col]
                if matrix[row - 1][col - 1] == '1':
                    dp[col] = min(dp[col - 1], dp[col], prev) + 1
                    maxLen = max(maxLen, dp[col])
                else:
                    dp[col] = 0
                prev = temp
        return maxLen * maxLen

