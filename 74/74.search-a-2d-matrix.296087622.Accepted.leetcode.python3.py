class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        row = len(matrix)
        column = len(matrix[0])
        i, j = 0, column - 1
        while i < row and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False

