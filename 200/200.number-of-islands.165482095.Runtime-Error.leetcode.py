class Solution(object):
    def numIslands(self, grid):
        def dfs(grid, row, col):
            if row < 0 or row >= self.m or col < 0 or col >= self.n:
                return

            grid[row][col] = '0'
            dfs(grid, row, col + 1)
            dfs(grid, row, col - 1)
            dfs(grid, row + 1, col)
            dfs(grid, row - 1, col)

        if not grid or len(grid) == 0:
            return 0

        self.m = len(grid)
        self.n = len(grid[0])
        result = 0

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] != '1':
                    continue

                result += 1
                print('result --> %s' % result)
                dfs(grid, i, j)
        return result

