class Solution(object):
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]
        result = []
        for i in range(numRows):
            row = [1] * (i + 1)
            result.append(row)
            for j in range(1, len(row) - 1):
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        return result

