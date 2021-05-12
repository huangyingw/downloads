class Solution(object):
    def wallsAndGates(self, rooms):
        if not rooms or not rooms[0]:
            return
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    self.bfs(rooms, i, j, m, n, 1)

    def bfs(self, rooms, i, j, m, n, distance):
        coords = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for coord in coords:
            newI, newJ = i + coord[0], j + coord[1]
            if newI in range(0, m) and newJ in range(0, n) and rooms[newI][newJ] > distance:
                rooms[newI][newJ] = distance
                self.bfs(rooms, newI, newJ, m, n, distance + 1)

