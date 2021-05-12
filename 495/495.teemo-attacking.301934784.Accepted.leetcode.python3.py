class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        return sum(min(duration, b - a) for a, b in zip(timeSeries, timeSeries[1:] + [10e7]))

