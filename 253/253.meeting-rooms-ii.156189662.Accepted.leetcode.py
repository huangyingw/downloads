class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        class Point:
            def __init__(self, time, flag):
                self.time = time
                self.flag = flag

            def __lt__(self, other):
                if self.time < other.time:
                    return True
                elif self.time > other.time:
                    return False
                elif self.flag == 'end':
                    return True
                else:
                    return False
        points = []
        for interval in intervals:
            points.append(Point(interval.start, 'start'))
            points.append(Point(interval.end, 'end'))
        points.sort()
        count = 0
        result = 0
        for point in points:
            if point.flag == 'start':
                count += 1
                result = max(result, count)
            else:
                count -= 1
        return result

