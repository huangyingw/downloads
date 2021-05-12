class ZigzagIterator(object):

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.pointer = 0
        if len(v1) != 0:
            self.l = 0
        else:
            self.l = 1
        self.x = 0

    def next(self):
        n = None
        if self.l == 0:
            n = self.v1[self.x]
            if self.x < len(self.v2):
                self.l = 1
                # keep self.x same
            else:
                # keep self.l same
                self.x += 1
        else:
            n = self.v2[self.x]
            if self.x < len(self.v1) - 1:
                self.l = 0
                self.x += 1
            else:
                self.x += 1

        self.pointer += 1
        return n

    def hasNext(self):
        return self.pointer < len(self.v1) + len(self.v2)

