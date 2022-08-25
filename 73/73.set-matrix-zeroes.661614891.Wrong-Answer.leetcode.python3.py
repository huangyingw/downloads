class Solution:
    def setZeroes(self, matrix):
        point_set = set()
        rows = len(matrix)
        columns = len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    if i >= 1:
                        point_set.add((i - 1, j))
                    if i <= rows - 2:
                        point_set.add((i + 1, j))
                    if j >= 1:
                        point_set.add((i, j - 1))
                    if j <= columns - 2:
                        point_set.add((i, j + 1))
        for (r, c) in point_set:
            matrix[r][c] = 0

