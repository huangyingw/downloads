class Solution:
    def setZeroes(self, matrix):
        m, n, firstRowHasZero = len(matrix), len(matrix[0]), not all(matrix[0])
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        for i in range(1, m):
            for j in range(n - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if firstRowHasZero:
            matrix[0] = [0] * n

