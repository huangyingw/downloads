class Solution(object):
    def constructRectangle(self, area):
        bondary = int(area**0.5)
        for i in range(bondary, 0, -1):
            if area % i == 0:
                return [area // i, i]

