class PeekingIterator(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.cur = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        return self.cur

    def next(self):
        val = self.cur
        self.cur = self.iterator.next() if self.iterator.hasNext() else None
        return val

    def hasNext(self):
        return self.cur is not None

