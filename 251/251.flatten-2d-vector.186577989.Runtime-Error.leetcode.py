class Vector2D(object):

    def __init__(self, vec2d):
        self.col = 0
        self.row = 0
        self.data = vec2d

    def next(self):
        result = self.data[self.row][self.col]
        self.col += 1

        if self.col == len(self.data[self.row]):
            self.row += 1
            self.col = 0

        return result

    def hasNext(self):
        return self.data and self.data[0] and self.row < len(self.data)

