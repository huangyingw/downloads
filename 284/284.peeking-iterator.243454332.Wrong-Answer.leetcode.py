class PeekingIterator(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.cur = self.iterator.next() if self.iterator.hasNext else None
        print('self.cur 1 --> %s' % (self.cur))

    def peek(self):
        return self.cur

    def next(self):
        val = self.cur
        if self.iterator.hasNext():
            self.cur = self.iterator.next()
            print('self.cur 2 --> %s' % (self.cur))
        return val

    def hasNext(self):
        return self.cur is not None

