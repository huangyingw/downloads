class Solution(object):
    def merge(self, intervals):
        if intervals is None:
            return
        ls = len(intervals)
        if ls <= 1:
            return intervals
        intervals.sort(key=lambda x: x.start)
        pos = 0
        while pos < len(intervals) - 1:
            if intervals[pos].end >= intervals[pos + 1].start:
                next = intervals.pop(pos + 1)
                if next.end > intervals[pos].end:
                    intervals[pos].end = next.end
            else:
                pos += 1
        return intervals

