class NestedIterator(object):
    def __init__(self, nestedList):
        self.queue = []
        for i in range(len(nestedList)):
            self.queue.append(nestedList[i])

    def next(self):
        return self.queue.pop(0).getInteger()

    def hasNext(self):
        while self.queue:
            top = self.queue[0]
            if top.isInteger():
                return True
            curr = self.queue.pop(0)
            nlist = curr.getList()
            for i in range(len(nlist)):
                self.queue.insert(i, nlist[i])
        return False

