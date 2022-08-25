class Solution(object):
    def merge(self, intervals):
        if intervals is None:
            return
        ls = len(intervals)
        if ls <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        pos = 0
        while pos < len(intervals) - 1:
            if intervals[pos][1] >= intervals[pos + 1][0]:
                next = intervals.pop(pos + 1)
                if next[1] > intervals[pos][1]:
                    intervals[pos][1] = next[1]
            else:
                pos += 1
        return intervals

