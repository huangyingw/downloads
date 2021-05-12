class MovingAverage(object):
    def __init__(self, size):
        self.size = size
        self.curr_range = []

    def next(self, val):
        if len(self.curr_range) == self.size:
            self.curr_range.pop(0)
        self.curr_range.append(val)
        return sum(self.curr_range) * 1.0 // len(self.curr_range)

