class Solution(object):
    def searchMatrix(self, matrix, target):
        left, right = 0, len(matrix[0]) * len(matrix) - 1

        while left + 1 < right:
            mid = (left + right) / 2
            row = mid / len(matrix[0])
            col = mid % len(matrix[0])

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid
            else:
                left = mid

        return matrix[left / len(matrix[0])][left % len(matrix[0])] == target or matrix[right / len(matrix[0])][right % len(matrix[0])] == target

