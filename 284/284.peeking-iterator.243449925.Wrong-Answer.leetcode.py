class PeekingIterator(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.n = None

    def peek(self):
        return self.n

    def next(self):
        if self.n != None:
            tmp = self.n
            self.n = None
            return tmp
        else:
            self.n = self.iterator.next()
            return self.n

    def hasNext(self):
        if self.n != None:
            return True
        else:
            return self.iterator.hasNext()

