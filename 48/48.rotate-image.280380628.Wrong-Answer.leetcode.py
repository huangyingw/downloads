class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        m = n // 2
        for i in range(n / 2):
            for j in range(m):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = temp

