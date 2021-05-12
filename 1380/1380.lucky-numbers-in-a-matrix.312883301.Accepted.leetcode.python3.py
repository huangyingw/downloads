class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        res = []
        points = set()
        for row in range(len(matrix)):
            min_points = {(row, 0)}
            min_number = matrix[row][0]
            for j in range(1, len(matrix[row])):
                if matrix[row][j] < min_number:
                    min_number = matrix[row][j]
                    min_points = {(row, j)}
                elif matrix[row][j] == min_number:
                    min_points.add((row, j))
            points.update(min_points)

        for col in range(len(matrix[0])):
            max_points = {(0, col)}
            max_number = matrix[0][col]
            for j in range(len(matrix)):
                if matrix[j][col] > max_number:
                    max_number = matrix[j][col]
                    max_points = {(j, col)}
                elif matrix[j][col] == max_number:
                    max_points.add((j, col))

            for point in max_points:
                if point in points:
                    res.append(matrix[point[0]][point[1]])
        return res

