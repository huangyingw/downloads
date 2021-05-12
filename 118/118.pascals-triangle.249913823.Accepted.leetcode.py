class Solution:
    def generate(self, numRows):
        triag = [[0]]
        row = []
        for rsize in range(1, numRows + 1):
            row = [0 for i in range(rsize)]
            row[0] = row[-1] = 1
            for i in range(1, rsize - 1):
                row[i] = triag[-1][i] + triag[-1][i - 1]
            triag.append(row)
        return triag[1:]

