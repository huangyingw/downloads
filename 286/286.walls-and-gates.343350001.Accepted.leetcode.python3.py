class Solution(object):
    def dfs(self, r, x, y, depth):
        if x < 0 or y < 0 or x >= len(r) or y >= len(r[0]):
            return
        if r[x][y] == -1 or r[x][y] == 0 or r[x][y] <= depth:
            return
        if r[x][y] > depth or r[x][y] == Inf:
            r[x][y] = depth
        self.dfs(r, x - 1, y, depth + 1)
        self.dfs(r, x + 1, y, depth + 1)
        self.dfs(r, x, y - 1, depth + 1)
        self.dfs(r, x, y + 1, depth + 1)

    def wallsAndGates(self, rooms):
        for x in range(0, len(rooms)):
            for y in range(0, len(rooms[0])):
                if rooms[x][y] == 0:
                    self.dfs(rooms, x - 1, y, 1)
                    self.dfs(rooms, x + 1, y, 1)
                    self.dfs(rooms, x, y - 1, 1)
                    self.dfs(rooms, x, y + 1, 1)

