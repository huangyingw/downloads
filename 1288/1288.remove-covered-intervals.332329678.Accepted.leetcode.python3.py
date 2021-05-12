class Solution(object):
    def removeCoveredIntervals(self, intervals):
        stack = []
        intervals.sort(key=lambda x: [x[0], -x[1]])
        for interval in intervals:
            if not stack or stack[-1][1] < interval[1]:
                stack.append(interval)
        return len(stack)

