class compare(object):
    def __init__(self, interval):
        self.interval = interval

    def __lt__(self, other):
        if self.interval[0] == other.interval[0]:
            return self.interval[1] < other.interval[1]
        return self.interval[0] < other.interval[1]


class Solution(object):
    def merge(self, intervals):
        intervals = sorted(intervals, key=compare)
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

