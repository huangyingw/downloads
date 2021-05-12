class ZigzagIterator(object):
    def __init__(self, v1, v2):
        self.lists = list()
        self.numLists = 0
        if len(v1) > 0:
            self.lists.append(v1)
            if len(v2) > 0:
                self.lists.append(v2)
            self.numLists = len(self.lists)
            self.counters = [0] * self.numLists
            self.listCounter = 0

    def next(self):
        res = self.lists[self.listCounter][self.counters[self.listCounter]]
        if self.counters[self.listCounter] == len(self.lists[self.listCounter]) - 1:
            del self.counters[self.listCounter]
            del self.lists[self.listCounter]
            self.numLists -= 1
        else:
            self.counters[self.listCounter] += 1
            self.listCounter += 1
        if self.listCounter == self.numLists:
            self.listCounter = 0
        return res

    def hasNext(self):
        return self.numLists > 0

