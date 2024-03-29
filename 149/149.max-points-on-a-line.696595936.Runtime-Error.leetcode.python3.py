class Solution(object):
    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a % b)

    def maxPoints(self, points):
        result = 0
        for i in range(0, len(points)):
            m = {}
            duplicate = 1
            for j in range(i + 1, len(points)):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    duplicate += 1
                    continue
                dx = points[j].x - points[i][0]
                dy = points[j][1] - points[i].y
                d = self.gcd(dx, dy)
                t = {}
                t[dx // d] = dy // d
                m[t] = m.get(t, 0) + 1
            result = max(result, duplicate)
            for value in m.values():
                result = max(result, value + duplicate)
        return result

