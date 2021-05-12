class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        poisoned = 0
        timeSeries.append(float("inf"))
        for i in range(0, len(timeSeries) - 1):
            poisoned += min(duration, timeSeries[i + 1] - timeSeries[i])
        return poisoned

