class Solution(object):
    def spiralOrder(self, matrix):
        if matrix is None or len(matrix) == 0:
            return matrix
        m, n = len(matrix), len(matrix[0])
        return self.get_spiralOrder(matrix, 0, m - 1, 0, n - 1)

    def get_spiralOrder(self, matrix, r_start, r_end, c_start, c_end):
        if r_start > r_end or c_start > c_end:
            return []
        elif r_start == r_end:
            return matrix[r_start][c_start:c_end + 1]
        elif c_start == c_end:
            return [matrix[j][c_end] for j in range(r_start, r_end + 1)]
        curr = matrix[r_start][c_start:c_end + 1] + [matrix[j][c_end] for j in range(r_start + 1, r_end)] +\
            matrix[r_end][c_start:c_end + 1][::-1] +\
            [matrix[j][c_start] for j in reversed(range(r_start + 1, r_end))]
        res = curr + self.get_spiralOrder(matrix, r_start + 1, r_end - 1, c_start + 1, c_end - 1)
        return res

