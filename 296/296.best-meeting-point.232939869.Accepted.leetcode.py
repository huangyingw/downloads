class Solution(object):
    def minTotalDistance(self, grid):
        rowGrid = grid  # 用于计算row中位置
        colGrid = zip(*grid)  # 用于计算col中位置

        total = 0
        for grid in rowGrid, colGrid:  # 因为distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|。所以可以把row，col单独计算，采用一维的思想，x，y分别计算
            tempGrid = []
            for position, point in enumerate(grid):
                tempGrid += [position] * sum(point)  # how many points in position
            for p in tempGrid:
                total += abs(p - tempGrid[len(tempGrid) / 2])  # each point to target point

        return total

