class Solution:
    def generateMatrix(self, n):
        ret = [[0] * n for _ in range(n)]
        i = j = d = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for x in range(1, n * n):
            ret[i][j] = x
            nextDir = dirs[d]
            while (i + nextDir[0] == -1) or (i + nextDir[0] == n) or (j + nextDir[1] == n) or (j + nextDir[1] == -1) or ret[i + nextDir[0]][j + nextDir[1]] != 0:
                d = (d + 1) % 4
                nextDir = dirs[d]
            i += nextDir[0]
            j += nextDir[1]
        ret[i][j] = n * n
        return ret

