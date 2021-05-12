class Solution(object):
    def minMeetingRooms(self, intervals):
        class Point:
            def __init__(self, time, flag):
                self.time = time
                self.flag = flag

        points = []

        for interval in intervals:
            points.append(Point(interval.start, 'start'))
            points.append(Point(interval.end, 'end'))

        points.sort(key=lambda point: point.time)
        count = 0
        result = 0

        for point in points:
            print("point.time --> %s\n" % point.time)
            print("point.flag --> %s\n" % point.flag)
            if point.flag == 'start':
                count += 1
                result = max(result, count)
            else:
                count -= 1

        return result

