class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix:
            return 0

        maxLen = 0
        dp = [[0] * (len(matrix[0]) + 1)] * (len(matrix) + 1)

        print('dp[0][1] --> %s' % (dp[0][1]))
        for row in range(1, len(matrix) + 1):
            print('dp[0][1] --> %s' % (dp[0][1]))
            for col in range(1, len(matrix[0]) + 1):
                print('dp[0][1] --> %s' % (dp[0][1]))
                if matrix[row - 1][col - 1] == '1':
                    dp[row][col] = min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1]) + 1
                else:
                    dp[row][col] = 0
                print('row --> %s' % row)
                print('col --> %s' % col)
                print('dp[0][1] --> %s' % (dp[0][1]))
                maxLen = max(maxLen, dp[row][col])

        return maxLen * maxLen

