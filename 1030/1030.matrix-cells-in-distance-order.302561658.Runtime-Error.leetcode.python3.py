class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        queue = deque()
        queue.append((r0, c0))
        result = []
        visited = set()
        while queue:
            r, c = queue.popleft()
            if r < 0 or r >= R or c < 0 or c >= C:
                continue
            if (r, c) in visited:
                continue
            result.append((r, c))
            visited.add((r, c))
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                queue.append((r + dr, c + dc))
        return result

