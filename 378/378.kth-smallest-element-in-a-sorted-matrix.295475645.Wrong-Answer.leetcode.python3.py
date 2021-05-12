class Solution(object):
    def kthSmallest(self, matrix, k):
        cols = len(matrix[0])
        row, col = len(matrix) - 1, 0
        while True:
            if row * cols + col > k:
                row -= 1
            elif row * cols + col < k:
                col += 1
            else:
                return matrix[row][col]

