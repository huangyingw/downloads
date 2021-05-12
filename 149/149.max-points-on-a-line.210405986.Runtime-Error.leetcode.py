class Solution(object):
    def maxPoints(self, points):
        result, n = 0, len(points)

        for i in range(0, n):
            duplicate = 1

            for j in range(i + 1, n):
                cnt = 0
                x1, y1 = points[i].x, points[i].y
                x2, y2 = points[j].x, points[j].y

                if x1 == x2 and y1 == y2:
                    duplicate += 1
                    continue

                for k in range(0, n):
                    x3 = points[k].x, y3 = points[k].y

                    if x1 * y2 + x2 * y3 + x3 * y1 - x3 * y2 - x2 * y1 - x1 * y3 == 0:
                        ++cnt
                result = max(result, cnt)
            result = max(result, duplicate)
        return result

