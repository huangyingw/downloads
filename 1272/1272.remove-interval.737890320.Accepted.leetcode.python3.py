class Solution(object):
    def removeInterval(self, intervals, toBeRemoved):
        remove_start, remove_end = toBeRemoved
        result = []
        for i, (start, end) in enumerate(intervals):
            if remove_start >= end:
                result.append([start, end])
            elif remove_end <= start:
                result += intervals[i:]
                break
            else:
                if remove_start > start:
                    result.append([start, remove_start])
                if remove_end < end:
                    result.append([remove_end, end])
        return result

