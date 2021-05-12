class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        roots = [-1] * (n * m)
        positions = [[i, j] for i in range(m) for j in range(n) if grid[i][j] == '1']
        result = 0
        neighbors = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        for p in positions:
            root = n * p[0] + p[1]
            roots[root] = root
            result += 1
            for nb in neighbors:
                x, y = p[0] + nb[0], p[1] + nb[1]
                nb_root = n * x + y
                if x < 0 or x >= m or y < 0 or y >= n or roots[nb_root] == -1:
                    continue
                nb_root = self.findRoot(roots, nb_root)
                if root != nb_root:
                    result -= 1
                    roots[root] = nb_root
                    root = nb_root
        return result

    def findRoot(self, roots, node):
        while node != roots[node]:
            roots[node] = roots[roots[node]]
            node = roots[roots[node]]
        return node

