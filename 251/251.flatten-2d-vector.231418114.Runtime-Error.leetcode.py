class Vector2D(object):

    def __init__(self, vec2d):
        self.vec = vec2d
        self.row = 0
        self.col = 0

        while self.row != len(self.vec):
            if len(self.vec[self.row]) != 0:
                self.col = 0
                break
            self.row += 1

    def next(self):
        ret = self.vec[self.row][self.col]
        self.col += 1
        return ret

    def hasNext(self):
        if self.row == len(self.vec):
            return False
        if self.col != len(self.vec[self.row]):
            return True
        else:
            self.row += 1
            while self.row != len(self.vec):
                if len(self.vec[self.row]) != 0:
                    self.col = 0
                    return True
                self.row += 1
            return False

