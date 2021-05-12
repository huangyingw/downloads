class Solution:
    def generateMatrix(self, n):
        seen = [[False] * n for _ in range(n)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for i in range(1, n * n + 1):
            seen[r][c] = i
            if r + dr[di] == -1 or r + dr[di] == n or c + dc[di] == -1 or c + dc[di] == n or not seen[r + dr[di]][c + dc[di]]:
                di = (di + 1) % 4
            r, c = r + dr[di], c + dc[di]
        return seen

