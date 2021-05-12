class Vector2D(object):

    def __init__(self, vec2d):
        self.i = iter(vec2d)

    def next(self):
        return self.val

    def hasNext(self):
        if not hasattr(self, 'j'):
            try:
                self.j = iter(self.i.next())
            except StopIteration:
                return False

        try:
            self.val = self.j.next()
        except StopIteration:
            del self.j
            return self.hasNext()
        return True

