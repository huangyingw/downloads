class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        if not matrix[0]:
            return False
        left = 0
        right = len(matrix) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            if matrix[mid][0] < target:
                left = mid
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                return True
        index = left
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[index][mid] < target:
                left = mid + 1
            elif matrix[index][mid] > target:
                right = mid - 1
            else:
                return True
        return False

