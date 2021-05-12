class ZigzagIterator(object):

    def __init__(self, v1, v2):
        self.l = []
        i = 0
        while i < max(len(v1), len(v2)):
            if i < len(v1):
                self.l.append(v1[i])
            if i < len(v2):
                self.l.append(v2[i])
            i += 1
        self.index = 0

    def next(self):
        cur = self.l[self.index]
        self.index += 1
        return cur

    def hasNext(self):
        if self.index < len(self.l):
            return True
        else:
            return False

