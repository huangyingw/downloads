class compare(object):
    def __init__(self, interval):
        self.interval = interval

    def __lt__(self, other):
        if self.interval.start == other.interval.start:
            return self.interval.end < other.interval.end
        return self.interval.start < other.interval.end


class Solution(object):
    def merge(self, intervals):
        intervals = sorted(intervals, key=compare)
        merged = []
        for interval in intervals:
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)
        return merged

