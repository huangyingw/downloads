class NumMatrix(object):
    def __init__(self, matrix):
        if matrix is None or len(matrix) == 0:
            return
        height, width = len(matrix), len(matrix[0])
        self.dp = [[0] * (width + 1) for i in range(height + 1)]
        for i in range(height):
            for j in range(width):
                self.dp[i + 1][j + 1] = self.dp[i + 1][j] + \
                    self.dp[i][j + 1] + matrix[i][j] - self.dp[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - \
            self.dp[row2 + 1][col1] + self.dp[row1][col1]

