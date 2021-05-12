class NestedIterator(object):
    def __init__(self, nestedList):
        self.stack = []
        for i in range(len(nestedList)):
            self.stack.append(nestedList[i])

    def next(self):
        return self.stack.pop(0).getInteger()

    def hasNext(self):
        while self.stack:
            top = self.stack[0]
            if top.isInteger():
                return True
            curr = self.stack.pop(0)
            nlist = curr.getList()
            for i in range(len(nlist)):
                self.stack.append(nlist[i])
        return False

