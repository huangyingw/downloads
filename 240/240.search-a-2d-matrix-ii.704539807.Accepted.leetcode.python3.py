class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        row, col = len(matrix) - 1, 0
        while row >= 0 and col < len(matrix[0]):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return False

