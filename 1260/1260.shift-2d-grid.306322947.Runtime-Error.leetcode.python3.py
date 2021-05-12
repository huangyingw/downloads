class Solution(object):
    def shiftGrid(self, grid, k):

        new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
        m = len(grid)
        n = len(grid[0])

        true_k = k % (m * n)

        move_i = true_k / n

        move_j = true_k % n
        for i in range(m):
            for j in range(n):
                new_i = i + move_i

                if move_j + j >= n:
                    new_i += 1
                new_i %= m
                new_j = (j + move_j) % n
                new_grid[new_i][new_j] = grid[i][j]
        return new_grid

