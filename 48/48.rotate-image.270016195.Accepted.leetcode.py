class Solution(object):
    def rotate(self, matrix):
        if matrix is None or len(matrix) == 1:
            return
        ls = len(matrix)
        for i in range(ls / 2):
            begin, end = i, ls - 1 - i
            for k in range(ls - 2 * i - 1):
                temp = matrix[end - k][begin]
                matrix[end - k][begin] = matrix[end][end - k]
                matrix[end][end - k] = matrix[begin + k][end]
                matrix[begin + k][end] = matrix[begin][begin + k]
                matrix[begin][begin + k] = temp
        return

