class Solution(object):
    def setZeroes(self, matrix):
        if not matrix:
            return
        m = len(matrix)
        if m == 0:
            return
        r = []
        c = []
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    r.append(i)
                    c.append(j)
        r = set(r)
        c = set(c)
        for i in r:
            for j in range(n):
                matrix[i][j] = 0
        for i in range(m):
            for j in c:
                matrix[i][j] = 0

