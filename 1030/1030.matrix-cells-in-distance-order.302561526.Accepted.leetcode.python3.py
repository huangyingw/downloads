class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        result = []
        for r in range(R):
            for c in range(C):
                result.append((r, c))
        return sorted(result, key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))

