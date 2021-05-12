class Solution():
    def minimumTotal(self, triangle):
        length = len(triangle)
        columns = len(triangle[length - 1])
        dp = [[0 for col in range(columns)] for row in range(length)]
        row_index = 0
        for row in range(length):
            col_index = 0
            for val in triangle[row]:
                dp[row_index][col_index] = val
                col_index += 1
            row_index += 1
        for row in range(length - 2, -1, -1):
            for col in range(row + 1):
                dp[row][col] += min(dp[row + 1][col + 1], dp[row + 1][col])
        return dp[0][0]

