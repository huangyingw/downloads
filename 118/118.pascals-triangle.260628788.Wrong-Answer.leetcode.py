class Solution(object):
    def generate(self, numRows):
        result = []
        for i in range(0, numRows + 1):
            result.append([1] * (i + 1))
            for j in range(1, i):
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        return result

