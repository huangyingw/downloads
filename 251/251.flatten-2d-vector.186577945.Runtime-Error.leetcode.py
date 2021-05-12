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
        print('self.data --> %s\n' % (self.data))
        print('len(self.data) --> %s\n' % (len(self.data)))
        print('len(self.data[0]) --> %s\n' % (len(self.data[0])))
        return self.data and self.data[0] and self.row < len(self.data)

