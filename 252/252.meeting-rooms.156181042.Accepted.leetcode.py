class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if not intervals:
            return True

        intervals.sort(key=lambda val: val.start)
        end = intervals[0].end

        for index in range(1, len(intervals)):
            if intervals[index].start < end:
                return False
            end = max(end, intervals[index].end)
        return True

