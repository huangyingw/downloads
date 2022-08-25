class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        first_col = False
        first_row = False
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(0, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(0, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

