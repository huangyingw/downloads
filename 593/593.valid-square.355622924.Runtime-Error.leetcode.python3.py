class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        def square_dist(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        points = [p1, p2, p3, p4]
        square_dists = set()
        for i in range(4):
            for j in range(i + 1, 4):
                square_dists.add(square_dist(points[i], points[j]))
        side = min(square_dists)
        if max(square_dists) != 2 * side:
            return False
        return square_dists.count(side) == 2 * square_dists.count(2 * side)

