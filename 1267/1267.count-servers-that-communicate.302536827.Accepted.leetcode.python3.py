class Solution(object):
    def countServers(self, grid):
        rows, cols = len(grid), len(grid[0])
        row_servers, cols_servers = [0] * rows, [0] * cols
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_servers[r] += 1
                    cols_servers[c] += 1
        result = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (row_servers[r] > 1 or cols_servers[c] > 1):
                    result += 1
        return result

