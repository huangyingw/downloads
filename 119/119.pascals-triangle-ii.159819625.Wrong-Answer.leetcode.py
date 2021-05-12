class Solution(object):
    def getRow(self, rowIndex):
        row = []

        for i in range(rowIndex):
            row.append(1)

            for j in range(i, 0, -1):
                row[i] += row[i - 1]
        return row

