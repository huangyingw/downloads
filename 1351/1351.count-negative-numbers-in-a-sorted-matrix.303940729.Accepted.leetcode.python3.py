class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row, column, count = m - 1, 0, 0
        while row >= 0 and column < n:
            if grid[row][column] < 0:
                count += (n - column)
                row -= 1
            else:
                column += 1
        return count


class Solution1:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    count += 1
        return count

