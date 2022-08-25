class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        start = newInterval.start
        end = newInterval.end
        res = []
        i = 0
        while i < len(intervals):
            if start <= intervals[i].end:
                if end < intervals[i].start:
                    break
                start = min(start, intervals[i].start)
                end = max(end, intervals[i].end)
            else:
                res.append(intervals[i])
            i += 1
        res.append(Interval(start, end))
        res += intervals[i:]
        return res

    def insert2(self, intervals, newInterval):
        s, e = newInterval.start, newInterval.end
        left = [inter for inter in intervals if inter.end < s]
        right = [inter for inter in intervals if inter.start > e]
        if len(left) + len(right) < len(intervals):
            start = min(intervals[len(left)].start, s)
            end = max(intervals[-len(right) - 1].end, e)
            newInterval = Interval(start, end)
        return left + [newInterval] + right

