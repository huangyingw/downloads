class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        if len(timeSeries) == 0:
            return 0
        return sum(min(duration, i - j) for i, j in zip(timeSeries[1:], timeSeries[:-1])) + duration

