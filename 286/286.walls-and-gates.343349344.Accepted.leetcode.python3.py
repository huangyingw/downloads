class Solution(object):
    def dfs(self, r, y, x, depth):
        if y < 0 or x < 0 or y >= len(r) or x >= len(r[0]):
            return
        if r[y][x] == -1 or r[y][x] == 0 or r[y][x] <= depth:
            return
        if r[y][x] > depth or r[y][x] == Inf:
            r[y][x] = depth
        self.dfs(r, y - 1, x, depth + 1)
        self.dfs(r, y + 1, x, depth + 1)
        self.dfs(r, y, x - 1, depth + 1)
        self.dfs(r, y, x + 1, depth + 1)

    def wallsAndGates(self, rooms):
        for y in range(0, len(rooms)):
            for x in range(0, len(rooms[0])):
                if rooms[y][x] == 0:
                    self.dfs(rooms, y - 1, x, 1)
                    self.dfs(rooms, y + 1, x, 1)
                    self.dfs(rooms, y, x - 1, 1)
                    self.dfs(rooms, y, x + 1, 1)

