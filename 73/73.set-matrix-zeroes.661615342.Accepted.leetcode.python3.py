class Solution:
    def setZeroes(self, matrix):
        if not matrix or not matrix[0]:
            return
        h = len(matrix)
        w = len(matrix[0])
        rows_to_remove = set()
        cols_to_remove = set()
        for i in range(h):
            if i not in rows_to_remove:
                for j in range(w):
                    if matrix[i][j] == 0:
                        rows_to_remove.add(i)
                        cols_to_remove.add(j)
        for i in rows_to_remove:
            for j in range(w):
                matrix[i][j] = 0
        for j in cols_to_remove:
            for i in range(h):
                matrix[i][j] = 0

