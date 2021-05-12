class Solution(object):
    def dfs(self, r, x, y, depth):
        if x in range(0, len(r)) and y in range(0, len(r[0])) and r[x][y] > depth:
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

