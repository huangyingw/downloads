class Solution(object):
    def getRow(self, rowIndex):
        row = []

        for i in range(rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
            row.append(1)
        return row

