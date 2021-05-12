class Solution(object):
    def canAttendMeetings(self, intervals):
        if not intervals:
            return True

        intervals.sort(key=lambda val: val.start)
        end = intervals[0].end

        for idx in range(1, len(intervals)):
            if end > intervals[idx].start:
                return False

            end = intervals[idx].end

        return True

