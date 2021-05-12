class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        res = []
        numbers = set()
        for row in range(len(matrix)):
            min_number = matrix[row][0]
            for j in range(1, len(matrix[row])):
                if matrix[row][j] < min_number:
                    min_number = matrix[row][j]
            numbers.add(min_number)

        for col in range(len(matrix[0])):
            max_number = matrix[0][col]
            for j in range(len(matrix)):
                if matrix[j][col] > max_number:
                    max_number = matrix[j][col]
            if max_number in numbers:
                res.append(max_number)
        return res

