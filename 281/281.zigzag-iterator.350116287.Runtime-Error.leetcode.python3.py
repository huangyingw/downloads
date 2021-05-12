class ZigzagIterator(object):

    def __init__(self, v1, v2):
        self.lists = list()
        if len(v1) > 0:
            self.lists.append(v1)
        if len(v2) > 0:
            self.lists.append(v2)

        self.numLists = len(self.lists)
        self.counters = [0] * self.numLists
        self.listIndex = 0

    def next(self):
        res = self.lists[self.listIndex][self.counters[self.listIndex]]
        if self.counters[self.listIndex] == len(self.lists[self.listIndex]) - 1:
            del self.counters[self.listIndex]
            del self.lists[self.listIndex]
            self.numLists -= 1
        else:
            self.counters[self.listIndex] += 1
            self.listIndex += 1
        self.listIndex %= self.numLists
        return res

    def hasNext(self):
        return self.numLists > 0

