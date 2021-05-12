class Solution:
    def generateMatrix(self, n):
        seen = [[False] * n for _ in range(n)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for i in range(1, n * n + 1):
            seen[r][c] = i
            if not (0 <= r + dr[di] < n and 0 <= c + dc[di] < n and not seen[r + dr[di]][c + dc[di]]):
                di = (di + 1) % 4
            r, c = r + dr[di], c + dc[di]
        return seen

