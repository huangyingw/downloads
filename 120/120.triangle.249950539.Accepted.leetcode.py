class Solution():
    def minimumTotal(self, triangle):
        length = len(triangle)
        columns = len(triangle[length - 1])
        matrix = [[0 for col in range(columns)] for row in range(length)]
        row_index = 0
        for row in range(length):
            elements = triangle[row]
            col_index = 0
            for val in elements:
                matrix[row_index][col_index] = val
                col_index += 1
            row_index += 1
        for row in range(length - 2, -1, -1):
            for col in range(row + 1):
                matrix[row][col] += min(matrix[row + 1][col + 1], matrix[row + 1][col])
        return matrix[0][0]

