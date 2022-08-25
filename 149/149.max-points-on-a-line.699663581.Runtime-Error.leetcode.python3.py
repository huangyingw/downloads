class Solution(object):
    def maxPoints(self, points):
        result, n = 0, len(points)
        for i in range(0, n):
            duplicate = 1
            for j in range(i + 1, n):
                cnt = 0
                x1 = points[i][0], y1 = points[i][1]
                x2 = points[j][0], y2 = points[j][1]
                if x1 == x2 and y1 == y2:
                    duplicate += 1
                    continue
                for k in range(0, n):
                    x3 = points[k][0], y3 = points[k][1]
                    if x1 * y2 + x2 * y3 + x3 * y1 - x3 * y2 - x2 * y1 - x1 * y3 == 0:
                        ++cnt
                result = max(result, cnt)
            result = max(result, duplicate)
        return result

